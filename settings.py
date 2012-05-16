# -*- coding: utf-8 -*-
DATABASE_NAME = u'domna'
PROJECT_NAME = u'domna'
SITE_NAME = u'Домна'
DEFAULT_FROM_EMAIL = u'support@domna.octweb.ru'

from config.base import *

try:
    from config.development import *
except ImportError:
    from config.production import *

TEMPLATE_DEBUG = DEBUG

INSTALLED_APPS += (
    'apps.siteblocks',
    'apps.pages',
    'apps.faq',
    'apps.newsboard',
    'apps.social',
    'apps.council',
    'apps.documents',
    #'apps.slider',

    'sorl.thumbnail',
    #'south',
    #'captcha',
)

MIDDLEWARE_CLASSES += (
    'apps.pages.middleware.PageFallbackMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'apps.pages.context_processors.meta',
    'apps.siteblocks.context_processors.settings',
)