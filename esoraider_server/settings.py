import os
from pathlib import Path

from dotenv import load_dotenv

dotenv_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path)

CLIENT_ID = os.environ.get('CLIENT_ID', '')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET', '')
DEBUG = os.environ.get('DEBUG') == 'True'
HEALTHCHECK_TOKEN = os.environ.get('HEALTHCHECK_TOKEN', 'braindead')
CORS_ALLOW_ORIGINS = os.environ.get(
    'CORS_ALLOW_ORIGINS',
    'http://localhost:8080 http://127.0.0.1:8080',  # default local dev
).split(' ')
