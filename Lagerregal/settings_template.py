# Django settings for Lagerregal project.
import os
from django.contrib.messages import constants as messages

DEBUG = True

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'database.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT =  '{0}/media'.format(os.getcwd())

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    '{0}/static'.format(os.getcwd()),
)

LOCALE_PATHS = (
    '{0}/locale'.format(os.getcwd()),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '@w_%5@z0kf8c@^=a++-awtkf^44)fk3r2qv2^m@9l+z5gm#vwo'

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'reversion.middleware.RevisionMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'users.middleware.TimezoneMiddleware'
)

ROOT_URLCONF = 'Lagerregal.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'Lagerregal.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '{0}/templates'.format(os.getcwd()),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'devices.context_processors.get_settings'
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader',
            ],
            'builtins': ['permission.templatetags.permissionif']
        },
    },
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'main',
    'devices',
    'network',
    'devicetypes',
    'devicegroups',
    'devicetags',
    'locations',
    'users',
    'api',
    'mail',
    'history',
    'reversion',
    'rest_framework',
    'permission',
    'debug_toolbar',
    'oauth2_provider',
)

LANGUAGES = (
  ('de', 'German'),
  ('en', 'English'),
)

AUTH_USER_MODEL = 'users.Lageruser'

SITE_NAME = "Lagerregal"

MESSAGE_TAGS = {
    messages.ERROR: 'alert',
}

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    )
}

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '{0}/mails'.format(os.getcwd())
DEFAULT_FROM_EMAIL = 'support@localhost'

INTERNAL_IPS = [
    "127.0.0.1",
]


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'permission.backends.PermissionBackend',
)

USE_LDAP = False

if USE_LDAP:
    AUTH_LDAP_SERVER_URI = ""
    AUTH_LDAP_BIND_DN = ""
    AUTH_LDAP_BIND_PASSWORD = ""
    AUTH_LDAP_USER_SEARCH = LDAPSearch("",
        ldap.SCOPE_SUBTREE, "")
    AUTH_LDAP_GROUP_SEARCH = LDAPSearch("",
        ldap.SCOPE_SUBTREE, '')

    LDAP_USER_SEARCH = ["", ldap.SCOPE_SUBTREE, ""]
    LDAP_GROUP_SEARCH = ["", ldap.SCOPE_SUBTREE, '']

    AUTH_LDAP_GROUP_TYPE = ActiveDirectoryGroupType()
    AUTH_LDAP_MIRROR_GROUPS  = True

    AUTH_LDAP_ATTR_NOSYNC = []
    AUTH_LDAP_USER_ATTR_MAP = {
        "first_name": "",
        "last_name": "",
        "email": ""
    }

    AUTH_LDAP_USER_FLAGS_BY_GROUP = {
        "is_staff":  "",
    }

    AUTH_LDAP_DEPARTMENT_FIELD = None
    AUTH_LDAP_DEPARTMENT_REGEX = None

USE_PUPPET = True

if USE_PUPPET:
    PUPPETDB_SETTINGS = {
        'host'          : 'puppetdb',
        'port'          : 8081,
        'cacert'        : '/var/lib/puppet/ssl/certs/ca.pem',
        'cert'          : '/var/lib/puppet/ssl/certs/<FQDN>.pem',
        'key'           : '/var/lib/puppet/ssl/private_keys/<FQDN>.pem',
        'req'           : '/pdb/query/v4/facts?',
        'query_fact'    : 'fact_containing_pk',
        'software_fact' : 'software',
    }

LABEL_TEMPLATES = {
    "device" :
    [
        "",
        ""
    ]
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

PUBLIC_DEVICES_FILTER = {}

# get more themes from https://bootswatch.com/ and download them to:
#   static/css/themes/<name>.min.css
THEMES = [
    'default',
    'darkly',
    'simplex',
    'superhero',
    'united',
    'paper',
]
