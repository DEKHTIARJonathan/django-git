# Django settings for django_git_tester project.
import os.path
import django

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ("Jonathan Dekhtiar", "contact@speleodb.com"),
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'a.db'             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

DJANGO_ROOT = django.__path__[0]
PROJECT_ROOT = os.path.dirname(__file__)

MEDIA_URL =  "/media/"
STATIC_URL =  "/static/"
MEDIA_ROOT = os.path.realpath(os.path.join(PROJECT_ROOT, "django_git/media"))
STATIC_ROOT = os.path.realpath(os.path.join(PROJECT_ROOT, "django_git/static"))

ADMIN_MEDIA_PREFIX = '/media/'
ADMIN_MEDIA_ROOT = os.path.realpath(os.path.join(DJANGO_ROOT, "contrib/admin/media/"))


# Make this unique, and don't share it with anybody.
SECRET_KEY = 'f6u7who_y1trniagg!scp7m4n0&e^)kb&=&w^&p1$=_4s&_vj4'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    # 'django.template.loaders.filesystem.load_template_source',
    #
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
    # 'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

#ROOT_URLCONF = 'django_git.urls'
ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, "templates"),
    os.path.join(PROJECT_ROOT, "django_git/templates"),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'bootstrap_toolkit',
    'django_git',
)

REPOS_ROOT = "/dev/shm/"
SERVE_MEDIA = True