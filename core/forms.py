from django import forms
from .models import Sign_up


class EmailSignupForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'type': 'email',
        'name': 'email',
        'id': 'email',
        'placeholder': 'Enter your e-mail address',
        'class': 'form-control'
    }), label='')

    class Meta:
        model = Sign_up
        fields = ('email',)


class ContactForms(forms.Form):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'email'
    }), required=True)
    subject = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'name': 'subject'
    }), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'name': 'message'
    }), required=True)