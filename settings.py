"""
Django settings for bigpeach project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import os
import environ


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    ENABLE_PATTERN_LIBRARY=(bool, False)
)
# reading .env file
environ.Env.read_env()

# False if not in os.environ
DEBUG = env('DEBUG')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'debug_toolbar',  # for dev only
    'tinymce',
    'crispy_forms',
    'robots',
    'core',
    'events',
    'social_rpa',
    'blog',
    'members',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'wsgi.application'

DATABASES = {
    # read os.environ['DATABASE_URL'] and raises ImproperlyConfigured exception if not found
    'default': env.db(),
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'core/static'),
    os.path.join(BASE_DIR, 'blog/static'),
]

STATIC_ROOT = env('STATIC_ROOT')

SITE_ID = 1

# TinyMCE
TINYMCE_DEFAULT_CONFIG = {'theme': 'advanced', }

# DEBUG TOOLBAR - NOT FOR PRODUCTION!
INTERNAL_IPS = [
    '127.0.0.1',
]

# django-crispy-forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# wysiwyg settings on admin
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,paste,searchreplace",
    'width': '100%',
    'height': 800
}

# email
if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'


ADMINS = [('PR', 'pryelluw@gmail.com')]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins', ],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['console', 'mail_admins', ],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['console', 'mail_admins', ],
            'level': 'DEBUG',
            'propagate': False,
        },
        'django.db.backends': {
            'handlers': ['console', 'mail_admins', ],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security.*': {
            'handlers': ['console', 'mail_admins', ],
            'level': 'ERROR',
            'propagate': False,
        },
        'core': {
            'handlers': ['console', 'mail_admins', ],
            'level': 'DEBUG',
        },
        'blog': {
            'handlers': ['console', 'mail_admins', ],
            'level': 'DEBUG',
        },
        'events': {
            'handlers': ['console', 'mail_admins', ],
            'level': 'DEBUG',
        },
        'members': {
            'handlers': ['console', 'mail_admins', ],
            'level': 'DEBUG',
        },
        'social_rpa': {
            'handlers': ['console', 'mail_admins', ],
            'level': 'DEBUG',
        },

    }
}

# django-pattern-library-settings

# note: for development only
# Do not enable on production!
# Security risk!
ENABLE_PATTERN_LIBRARY = env('ENABLE_PATTERN_LIBRARY')

if DEBUG and ENABLE_PATTERN_LIBRARY:
    
    INSTALLED_APPS = INSTALLED_APPS + ['pattern_library']

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
                "builtins": [
                    "pattern_library.loader_tags"
                ],
            },
        },
    ]
    
    PATTERN_LIBRARY = {
        # Groups of templates for the pattern library navigation. The keys
        # are the group titles and the values are lists of template name prefixes that will
        # be searched to populate the groups.
        "SECTIONS": (
            ("components", ["patterns/components"]),
            ("pages", ["patterns/pages"]),
        ),

        # Configure which files to detect as templates.
        "TEMPLATE_SUFFIX": ".html",

        # Set which template components should be rendered inside of,
        # so they may use page-level component dependencies like CSS.
        "PATTERN_BASE_TEMPLATE_NAME": "patterns/base_layout.html",

        # Any template in BASE_TEMPLATE_NAMES or any template that extends a template in
        # BASE_TEMPLATE_NAMES is a "page" and will be rendered as-is without being wrapped.
        "BASE_TEMPLATE_NAMES": ["patterns/base_page.html"],
    }
    


