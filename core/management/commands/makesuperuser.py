from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.db import transaction
import getpass
import secrets
import os

class Command(BaseCommand):
    help = "Create a superuser. Supports interactive prompts, env vars, or CLI options."

    def add_arguments(self, parser):
        parser.add_argument('--noinput', action='store_true', dest='noinput',
                            help='Do not prompt for input. Requires providing all fields via options or environment variables.')
        parser.add_argument('--username', dest='username', help='Specify the username for the superuser.')
        parser.add_argument('--email', dest='email', help='Specify the email for the superuser.')
        parser.add_argument('--password', dest='password', help='Specify the password for the superuser.')
        parser.add_argument('--random-password', action='store_true', dest='random_password',
                            help='Generate a random password and print it.')

    def handle(self, *args, **options):
        UserModel = get_user_model()
        username_field = getattr(UserModel, 'USERNAME_FIELD', 'username')
        required_fields = getattr(UserModel, 'REQUIRED_FIELDS', [])

        # Gather inputs from CLI options, env vars, or interactive prompts
        username = options.get('username') or os.environ.get('DJANGO_SUPERUSER_USERNAME')
        email = options.get('email') or os.environ.get('DJANGO_SUPERUSER_EMAIL')
        password = options.get('password') or os.environ.get('DJANGO_SUPERUSER_PASSWORD')
        noinput = options.get('noinput')
        random_password = options.get('random_password')

        if not username and not noinput:
            username = input(f'{username_field}: ').strip()

        if not username:
            raise CommandError(f'{username_field} is required (provide via --username or DJANGO_SUPERUSER_USERNAME)')

        # Check existence
        lookup = {username_field: username}
        if UserModel.objects.filter(**lookup).exists():
            self.stdout.write(self.style.WARNING(f'Superuser with {username_field}="{username}" already exists.'))
            return

        # Collect other required fields (except username)
        extra_fields = {}
        # handle email if it's required or provided
        email_field_name = getattr(UserModel, 'EMAIL_FIELD', 'email')
        if email or (email_field_name in required_fields) or 'email' in required_fields:
            if not email and not noinput:
                email = input('Email address: ').strip()
            if not email:
                raise CommandError('Email is required (provide via --email or DJANGO_SUPERUSER_EMAIL)')
            extra_fields[email_field_name] = email

        # Prompt for other REQUIRED_FIELDS
        for field in required_fields:
            if field == email_field_name:
                continue
            # try env var first
            env_key = f'DJANGO_SUPERUSER_{field.upper()}'
            val = os.environ.get(env_key)
            if not val and not noinput:
                val = input(f'{field}: ').strip()
            if not val:
                raise CommandError(f'{field} is required (provide via --{field} or {env_key})')
            extra_fields[field] = val

        # Password handling
        if random_password:
            password = secrets.token_urlsafe(16)
            self.stdout.write(self.style.NOTICE(f'Generated random password: {password}'))

        if not password:
            if noinput:
                raise CommandError('When using --noinput you must provide --password or set DJANGO_SUPERUSER_PASSWORD.')
            password = getpass.getpass()
            password2 = getpass.getpass(prompt='Password (again): ')
            if password != password2:
                raise CommandError('Passwords do not match.')

        # Create superuser in a transaction
        with transaction.atomic():
            create_kwargs = {username_field: username, **extra_fields}
            try:
                UserModel._default_manager.create_superuser(**{**create_kwargs, 'password': password})
            except TypeError:
                # fallback in case create_superuser signature differs
                user = UserModel(**create_kwargs)
                user.set_password(password)
                user.is_staff = True
                user.is_superuser = True
                user.save()

        self.stdout.write(self.style.SUCCESS(f'Superuser "{username}" created successfully.'))