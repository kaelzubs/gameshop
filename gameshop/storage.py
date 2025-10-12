from whitenoise.storage import CompressedManifestStaticFilesStorage

class WhiteNoiseStaticFilesStorage(CompressedManifestStaticFilesStorage):
    manifest_strict = False

class MediaStorage:
    location = 'media'
    file_overwrite = False
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    def _save(self, name, content):
        return super()._save(name, content)
    def url(self, name):
        return super().url(name)
    def exists(self, name):
        return super().exists(name)
    def delete(self, name):
        return super().delete(name)
    def listdir(self, path):
        return super().listdir(path)
    def size(self, name):
        return super().size(name)
    def accessed_time(self, name):
        return super().accessed_time(name)
    def created_time(self, name):
        return super().created_time(name)
    def modified_time(self, name):
        return super().modified_time(name)
    def get_available_name(self, name, max_length=None):
        return super().get_available_name(name, max_length)
    def path(self, name):
        return super().path(name)
    def get_valid_name(self, name):
        return super().get_valid_name(name)
    def get_directory_name(self, name):
        return super().get_directory_name(name)
    def get_file(self, name):
        return super().get_file(name)
    def list(self, path):
        return super().list(path)
    
