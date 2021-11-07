import os

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

API_PREFIX = '/api'

VERSION = '0.0.1'

dir_path = os.path.dirname(os.path.realpath(__file__))
root_dir = dir_path[:-3]

config = Config(f'{root_dir}.env')

IS_TEST = bool(os.getenv('IS_TEST', False))
DEBUG = config('DEBUG', cast=bool, default=False)

if IS_TEST:
    DATABASE_URL = f'sqlite:///{root_dir}' + config('TEST_DB_NAME', cast=str, default='test_app.db')
else:
    DATABASE_URL = f'sqlite:///{root_dir}' + config('DB_NAME', cast=str)

MAX_CONNECTIONS_COUNT = config('MAX_CONNECTIONS_COUNT', cast=int, default=10)
MIN_CONNECTIONS_COUNT = config('MIN_CONNECTIONS_COUNT', cast=int, default=10)

SECRET_KEY = config('SECRET_KEY', cast=Secret)

PROJECT_NAME = config('PROJECT_NAME', default='FastApi application example')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=CommaSeparatedStrings, default='')
