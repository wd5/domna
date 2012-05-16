# -*- coding: utf-8 -*-
from apps.newsboard.models import News
from django import template

register = template.Library()

@register.inclusion_tag("newsboard/block_news.html")
def block_news():
    news = News.objects.published()[:3]
    return {'news': news,}