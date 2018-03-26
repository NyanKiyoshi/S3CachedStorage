from uuid import uuid4


SECRET_KEY = 'you_saw_nothing.'

context_processors = []
loaders = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = [
    'S3CachedStorage.apps.S3CachedStorageConfig'
]

MY_BUCKET_S3_STORAGE_BACKEND_CACHE_DIR = '/tmp/my_bucket_cache-%s' % uuid4().hex
