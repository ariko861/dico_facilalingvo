from settings import *

DEBUG = False
TEMPLATE_DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w!9_wal*z&y!znncn!d(v%!n(as38c($tw2&sfrwur9x)i(nm*'


ALLOWED_HOSTS = ['dico.facilalingvo.com',
		'www.dico.facilalingvo.com',
		'dico.facilalingvo.pw',
		'www.dico.facilalingvo.pw',
		'localhost','127.0.0.1',
		'dico.facilalingvo.artnelson.webfactional.com',
		'www.dico.facilalingvo.artnelson.webfactional.com',
]

ACCOUNT_USERNAME_BLACKLIST =["admin","arcturus","arthuro"]



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'SSL0.OVH.NET'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'postmaster@facilalingvo.com'
EMAIL_HOST_PASSWORD='v10pTGbkj5WFMvyfUZam'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
