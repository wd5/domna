# -*- coding: utf-8 -*-
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
import os
from django.db import models
from apps.utils.managers import PublishedManager

class CouncilItem(models.Model):
    short_description =  models.TextField(verbose_name = u'название')
    description =  models.TextField(verbose_name = u'описание')
    date_add = models.DateTimeField(verbose_name = u'дата публикации', default = datetime.now)
    is_published = models.BooleanField(verbose_name = u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return self.short_description

    class Meta:
        ordering = ['-date_add']
        verbose_name = _(u'council_item')
        verbose_name_plural = _(u'council_items')

    def get_absolute_url(self):
        return u'/council/%s/' % self.id

    def get_attached_docs(self):
        return self.attached_doc_set.published()

class Attached_doc(models.Model):
    councilitem = models.ForeignKey(CouncilItem, verbose_name=u'запись')
    title = models.CharField(max_length=255, verbose_name=u'название')
    document = models.FileField(upload_to='councildocs/', verbose_name=u'прикрепляемый документ')
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)
    is_published = models.BooleanField(verbose_name = u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'attached_doc')
        verbose_name_plural = _(u'attached_docs')

    def get_file_path(self):
        return self.document.url

    def get_fmt_ext(self):
        extension = os.path.splitext(self.document.name)[1]
        extension = extension[1:]
        if extension in [u'pdf',u'doc',u'txt']:
            return u'fmt_%s' % extension
        else:
            return u'fmt_any'