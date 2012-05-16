# -*- coding: utf-8 -*-
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
import os
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey, TreeManager
from apps.utils.managers import PublishedManager

class DocumentCategory(MPTTModel):
    title = models.CharField(max_length=255, verbose_name=u'название')
    parent = TreeForeignKey('self', verbose_name=u'родительская категория', related_name='children', blank=True, null=True)
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)
    is_published = models.BooleanField(verbose_name = u'опубликовано', default=True)

    objects = TreeManager()

    class Meta:
        verbose_name =_(u'doc_category')
        verbose_name_plural =_(u'doc_categories')
        ordering = ['-order']

    class MPTTMeta:
        order_insertion_by = ['order']

    def __unicode__(self):
        if self.parent:
            return u'%s - %s' % (self.parent, self.title)
        else:
            return u'%s' % self.title

    def get_absolute_url(self):
        if self.parent:
            return u'/documents/%s/%s/' % (self.parent.id,self.id)
        else:
            return u'/documents/%s/' % self.id

    def get_documents(self):
        return self.document_set.published()

class Document(models.Model):
    documentcategory = models.ForeignKey(DocumentCategory, verbose_name=u'категория')
    title = models.CharField(max_length=255, verbose_name=u'название')
    file = models.FileField(upload_to='documents/', verbose_name=u'файл документа')
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)
    is_published = models.BooleanField(verbose_name = u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'document_item')
        verbose_name_plural = _(u'document_items')

    def get_fmt_ext(self):
        extension = os.path.splitext(self.file.name)[1]
        extension = extension[1:]
        if extension in [u'pdf',u'doc',u'txt']:
            return u'fmt_%s' % extension
        else:
            return u'fmt_any'

    def get_file_path(self):
        return self.file.url

