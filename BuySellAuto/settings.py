"""
Django settings for BuySellAuto project.

Generated by 'django-admin startproject' using Django 2.1.13.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&&uu6isrp70e_o#o=fjixy53l#ak9kr6kx$3p*$1ufc+1^l_gq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    # 'jet.dashboard',
    # 'jet',
    # 'admin_interface',
    # #'flat_responsive',  # only if django version < 2.0
    # #'flat',  # only if django version < 1.9
    # 'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'store.apps.StoreConfig',
    # 'froala_editor',
    'import_export',
    'tinymce',
    'businessdirectory',
    'aboutus',
    'agents',
    'orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'BuySellAuto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'BuySellAuto.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "store/static")
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'store/templates'),)

TINYMCE_FILEBROWSER = True

# User Settings
AUTH_USER_MODEL = 'store.User'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

#SENDGRID_API_KEY = os.getenv('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')
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_PORT = 25
# EMAIL_HOST_USER = 'khrispin'
# EMAIL_HOST_PASSWORD = '@thachurchboy1'
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'chrispinkay@gmail.com'

# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
# EMAIL_HOST_PASSWORD = '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'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# DEFAULT_FROM_EMAIL = 'noreply@buysellauto.com'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'chrispinkay@gmail.com'
EMAIL_HOST_PASSWORD = 'iyodlyaeiokjladh'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'noreply@buysellauto.com'

# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST = 'smtp-relay.sendinblue.com'
# EMAIL_HOST_USER = 'khrispinwhiteman@gmail.com'
# EMAIL_HOST_PASSWORD = 'gh8M0GE3JmKqVS5P'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST = 'in-v3.mailjet.com'
# EMAIL_HOST_USER = '0568eacc2d520f2c4e3967c2220f3053'
# EMAIL_HOST_PASSWORD = '12d78e48d5d6ab0e9c5b05c031af25b7'

# EMAIL_BACKEND = 'django_mailjet.backends.MailjetBackend'
# MAILJET_API_KEY = '0568eacc2d520f2c4e3967c2220f3053'
# MAILJET_API_SECRET = '12d78e48d5d6ab0e9c5b05c031af25b7'

#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
#xsmtpsib-56d88994de4b28dc584914ab5cd2f7851e242b8136786d203fe73e5de68d52ff-DZNqwPgJYEmIAUtX
