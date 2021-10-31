import os

from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings, Secret

API_PREFIX = '/api'

VERSION = '0.0.1'

dir_path = os.path.dirname(os.path.realpath(__file__))

config = Config(f'{dir_path[:-3]}.env')

DEBUG = config('DEBUG', cast=bool, default=False)
DATABASE_URL = config('DB_CONNECTION', cast=str)
MAX_CONNECTIONS_COUNT = config('MAX_CONNECTIONS_COUNT', cast=int, default=10)
MIN_CONNECTIONS_COUNT = config('MIN_CONNECTIONS_COUNT', cast=int, default=10)

SECRET_KEY = config('SECRET_KEY', cast=Secret)

PROJECT_NAME = config('PROJECT_NAME', default='FastApi application example')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=CommaSeparatedStrings, default='')
