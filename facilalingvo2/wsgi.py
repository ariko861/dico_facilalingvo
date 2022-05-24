"""
WSGI config for facilalingvo2 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os,sys
import time
import traceback
import signal

sys.path.append('home/facilalingvo2')

os.environ['DJANGO_SETTINGS_MODULE'] = 'facilalingvo2.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "facilalingvo2.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
