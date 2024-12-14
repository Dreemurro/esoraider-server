import os
from os.path import dirname, join

from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CLIENT_ID = os.environ.get('CLIENT_ID', '')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET', '')
DEBUG = os.environ.get('DEBUG') == 'True'
HEALTHCHECK_TOKEN = os.environ.get('HEALTHCHECK_TOKEN', 'braindead')
