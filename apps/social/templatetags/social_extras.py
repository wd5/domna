# -*- coding: utf-8 -*-
from apps.social.models import SocialService
from django import template

register = template.Library()

@register.inclusion_tag("social/block_social_service.html")
def block_social_service():
    try:
        socServices = SocialService.objects.published()
    except:
        socServices = False
    return {'socServices': socServices}
