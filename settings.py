import os

from shopify_settings import *

SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

SHOPIFY_API_KEY = 'e7419e336fd63f54567a075d136f3fa1'
SHOPIFY_API_SECRET = '45c72d8d9cf56e13c9b46c841e24ca8d'

try:
    from djangoappengine.settings_base import *
    USING_APP_ENGINE = True
except ImportError:
    USING_APP_ENGINE = False

    DEBUG = True
    TEMPLATE_DEBUG = DEBUG

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', '
            'NAME': os.path.join(SITE_ROOT, 'db-development.sqlite3'),
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',  # Set to empty string for localhost. Not used with
            'PORT': '',                      # Set to empty string for default. Not used with sq
        }
    }

    SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'static'),
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '#w%yp9_5wnupojr=4o0mwap#!)y=q9ovu=o#xnytga7u5^bf27'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'shopify_app.context_processors.current_shop',
)
if not USING_APP_ENGINE:
    TEMPLATE_CONTEXT_PROCESSORS += (
            'django.core.context_processors.static',
    )

MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'shopify_app.middleware.LoginProtection',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__), 'templates'),
                 os.path.join(BASE_DIR, '../../templates'),
                 os.path.join(BASE_DIR, '../templates'),
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django.core.context_processors.csrf',
            ],
            'builtins': [
                'django.contrib.staticfiles.templatetags.staticfiles',
            ],
        },
    },
]
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'home',
    'shopify_app',
)
if USING_APP_ENGINE:
    INSTALLED_APPS += (
        'djangoappengine',
        'djangotoolbox',
    )
else:
    INSTALLED_APPS += (
        'django.contrib.sites',
        'django.contrib.staticfiles',
    )

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
