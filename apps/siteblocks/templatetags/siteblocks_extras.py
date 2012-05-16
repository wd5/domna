# -*- coding: utf-8 -*-
from apps.siteblocks.models import SiteMenu, Settings
from apps.documents.models import DocumentCategory
from django import template

register = template.Library()

@register.inclusion_tag("siteblocks/block_menu.html")
def block_menu(url,position):
    url = url.split('/')

    if url[1]:
        current = u'/%s/' % url[1]
    else:
        current = u'/'
    menu = SiteMenu.objects.published()
    categdoc = DocumentCategory.objects.filter(is_published = True, parent = None)
    return {'menu': menu, 'current': current, 'categdoc': categdoc, 'position': position,}

@register.inclusion_tag("siteblocks/block_setting.html")
def block_static(name):
    try:
        setting = Settings.objects.get(name = name)
    except Settings.DoesNotExist:
        setting = False
    return {'block': block,}
