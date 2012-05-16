# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from pytils.translit import slugify
from apps.utils.managers import PublishedManager

class News(models.Model):
    short_text = models.TextField(
        verbose_name = u'анонс',
    )
    text = models.TextField(
        verbose_name = u'текст',
    )
    is_published = models.BooleanField(
        verbose_name = u'опубликовано',
        default = True,
    )
    date_add = models.DateTimeField(
        verbose_name = u'дата создания',
        default = datetime.now
    )
    # Managers
    objects = PublishedManager()

    class Meta:
        ordering = ['-date_add', '-id',]
        verbose_name =_(u'news_item')
        verbose_name_plural =_(u'news_items')
        get_latest_by = 'date_add'

    def __unicode__(self):
        return self.short_text