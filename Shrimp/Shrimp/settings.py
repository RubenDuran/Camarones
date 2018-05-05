"""
Django settings for Shrimp project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import sys
from oscar.defaults import *
from oscar import get_core_apps
from oscar import OSCAR_MAIN_TEMPLATE_DIR

PY3 = sys.version_info >= (3, 0)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)

# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5a61u7e9x2pzcw()o8h9r*6&6e2i7sfoetcgxd!@l#5u=!mr9y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

ADMINS = (
    ('Ruben Duran', 'rd@rubenduran.net'),
)
EMAIL_SUBJECT_PREFIX = '[Ruben sandbox] '
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MANAGERS = ADMINS

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # added for oscar
    'django.contrib.sites',
    'django.contrib.flatpages',
    # ----
    'apps.shrimp',
    'apps.shrimp_store',
    # added for oscar
    'compressor',
    'widget_tweaks',
    # 'apps.gateway',     # For allowing dashboard access
    # 'debug_toolbar',
    'template_timings_panel',
    # 'south',
    # 'rosetta',          # For i18n testing
] + get_core_apps()

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # oscar
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'Shrimp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 OSCAR_MAIN_TEMPLATE_DIR
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # oscar add ons
                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]

WSGI_APPLICATION = 'Shrimp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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

DEBUG_TOOLBAR_PATCH_SETTINGS = False
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'template_timings_panel.panels.TemplateTimings.TemplateTimings',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

# Haystack settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
    },
}

USE_LESS = False

COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)
COMPRESS_OFFLINE_CONTEXT = {
    'STATIC_URL': 'STATIC_URL',
    'use_less': USE_LESS,
}

# We do this to work around an issue in compressor where the LESS files are
# compiled but compression isn't enabled.  When this happens, the relative URL
# is wrong between the generated CSS file and other assets:
# https://github.com/jezdez/django_compressor/issues/226
COMPRESS_OUTPUT_DIR = 'oscar'


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

MEDIA_ROOT = location("public/media")

MEDIA_URL = '/media/'

STATIC_URL = '/static/'
# oscar add on
STATIC_ROOT = location('public/static')
STATICFILES_DIRS = (
    location('static/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

if PY3:
    # Template timings panel doesn't work with Python 3 atm
    # https://github.com/orf/django-debug-toolbar-template-timings/issues/18
    INSTALLED_APPS.remove('template_timings_panel')
    DEBUG_TOOLBAR_PANELS.remove(
        'template_timings_panel.panels.TemplateTimings.TemplateTimings')

    # Meta
# ====

OSCAR_SHOP_TAGLINE = 'Sandbox'

OSCAR_RECENTLY_VIEWED_PRODUCTS = 20
OSCAR_ALLOW_ANON_CHECKOUT = True

# This is added to each template context by the core context processor.  It is
# useful for test/stage/qa sites where you want to show the version of the site
# in the page title.
DISPLAY_VERSION = False


# Order processing
# ================

# Some sample order/line status settings
OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
    'Processed': (),
}


# LESS/CSS/statics
# ================

# We default to using CSS files, rather than the LESS files that generate them.
# If you want to develop Oscar's CSS, then set USE_LESS=True and
# COMPRESS_ENABLED=False in your settings_local module and ensure you have
# 'lessc' installed.  You can do this by running:
#
#    pip install -r requirements_less.txt
#
# which will install node.js and less in your virtualenv.

USE_LESS = False

COMPRESS_ENABLED = True
COMPRESS_PRECOMPILERS = (
    ('text/less', 'lessc {infile} {outfile}'),
)
COMPRESS_OFFLINE_CONTEXT = {
    'STATIC_URL': 'STATIC_URL',
    'use_less': USE_LESS,
}

# We do this to work around an issue in compressor where the LESS files are
# compiled but compression isn't enabled.  When this happens, the relative URL
# is wrong between the generated CSS file and other assets:
# https://github.com/jezdez/django_compressor/issues/226
COMPRESS_OUTPUT_DIR = 'oscar'

# Logging
# =======

LOG_ROOT = location('logs')
# Ensure log root exists
if not os.path.exists(LOG_ROOT):
    os.mkdir(LOG_ROOT)

# Sorl
# ====

THUMBNAIL_DEBUG = True
THUMBNAIL_KEY_PREFIX = 'oscar-sandbox'

# Use a custom KV store to handle integrity error
THUMBNAIL_KVSTORE = 'oscar.sorl_kvstore.ConcurrentKVStore'

# Django 1.6 has switched to JSON serializing for security reasons, but it does not
# serialize Models. We should resolve this by extending the
# django/core/serializers/json.Serializer to have the `dumps` function. Also
# in tests/config.py
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# Try and import local settings which can be used to override any of the above.
try:
    from settings_local import *
except ImportError:
    pass
