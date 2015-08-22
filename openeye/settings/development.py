# -*- coding: utf-8 -*-
from .base import *

DEBUG = True

DB_USER = get_env_variable('DB_USER')
DB_PASS = get_env_variable('DB_PASS')

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'openeye',
        'USER': DB_USER,
        'PASSWORD': DB_PASS,
        'HOST': 'localhost',
        'PORT': '3307',
    }
}
