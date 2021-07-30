import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
DEBUG = os.environ.get('DEBUG') == 'True'
SHOW_ERROR_DETAILS = os.environ.get('SHOW_ERROR_DETAILS') == 'True'
