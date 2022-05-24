"""
Django settings for facilalingvo2 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.utils.translation import ugettext_lazy as _

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w!9_wal*z&y!znncn!d(v%!n(as38c($tw2&sfrwur9x)i(nm*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['dico.facilalingvo.com',
		'www.dico.facilalingvo.com',
		'dico.facilalingvo.pw',
		'www.dico.facilalingvo.pw',
		'localhost','127.0.0.1',
		'dico.facilalingvo.artnelson.webfactional.com',
		'www.dico.facilalingvo.artnelson.webfactional.com',
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'multidico',
    'django.contrib.sites',
    'import_export',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
#    'allauth.socialaccount.providers.amazon',
#    'allauth.socialaccount.providers.angellist',
#    'allauth.socialaccount.providers.bitbucket',
#    'allauth.socialaccount.providers.bitly',
#    'allauth.socialaccount.providers.coinbase',
#    'allauth.socialaccount.providers.dropbox',
#    'allauth.socialaccount.providers.dropbox_oauth2',
#    'allauth.socialaccount.providers.evernote',
#    'allauth.socialaccount.providers.facebook',
#    'allauth.socialaccount.providers.flickr',
#    'allauth.socialaccount.providers.feedly',
#    'allauth.socialaccount.providers.fxa',
#    'allauth.socialaccount.providers.github',
#    'allauth.socialaccount.providers.google',
#    'allauth.socialaccount.providers.hubic',
#    'allauth.socialaccount.providers.instagram',
#    'allauth.socialaccount.providers.linkedin',
#    'allauth.socialaccount.providers.linkedin_oauth2',
#    'allauth.socialaccount.providers.odnoklassniki',
#    'allauth.socialaccount.providers.openid',
#    'allauth.socialaccount.providers.persona',
#    'allauth.socialaccount.providers.soundcloud',
#    'allauth.socialaccount.providers.spotify',
#    'allauth.socialaccount.providers.stackexchange',
#    'allauth.socialaccount.providers.tumblr',
#    'allauth.socialaccount.providers.twitch',
#    'allauth.socialaccount.providers.twitter',
#    'allauth.socialaccount.providers.vimeo',
#    'allauth.socialaccount.providers.vk',
#    'allauth.socialaccount.providers.weibo',
#    'allauth.socialaccount.providers.xing',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.i18n',
  'django.core.context_processors.request',
  #'allauth.account.context_processors.account',
  #'allauth.socialaccount.context_processors.socialaccount',
)


ROOT_URLCONF = 'facilalingvo2.urls'

WSGI_APPLICATION = 'facilalingvo2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

LANGUAGES = (
        ('fr', _('French')),
        ('en', _('English')),
)

LOCALE_PATHS = (
	os.path.join(os.path.dirname(__file__), 'locale').replace('\\','/'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'facilalingvo2/templates'),
)

STATIC_ROOT = '/home/artnelson/webapps/static_dico_facilalingvo/'

STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/st$
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.dirname(__file__),'static').replace('\\','/'),
)

AUTHENTICATION_BACKENDS = (

    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',

)


SITE_ID = 1

# auth and allauth settings

LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'SCOPE': ['email', 'publish_stream'],
        'METHOD': 'js_sdk'  # instead of 'oauth2'
    }
}
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_USERNAME_BLACKLIST =["admin","arcturus","arthuro"]



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'SSL0.OVH.NET'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'postmaster@facilalingvo.com'
EMAIL_HOST_PASSWORD='v10pTGbkj5WFMvyfUZam'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
