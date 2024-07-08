import os
from dotenv import load_dotenv

DJANGO_ENV = os.getenv('DJANGO_ENV', 'local')

if DJANGO_ENV == 'production':
    settings_module = 'speech_processing_backend.settings.production'
elif DJANGO_ENV == 'staging':
    settings_module = 'speech_processing_backend.settings.staging'
else:
    settings_module = 'speech_processing_backend.settings.local'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
