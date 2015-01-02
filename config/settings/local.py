import os
from .base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += ("debug_toolbar", )

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
