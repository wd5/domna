# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
import os
from django.db import models
from sorl.thumbnail import ImageField as sorl_ImageField
from apps.utils.managers import PublishedManager
from pytils.translit import translify

class SocialService(models.Model):
    title = models.CharField(max_length=120, verbose_name=u'название социальной услуги')
    description =  models.TextField(verbose_name = u'описание услуги')
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)
    is_published = models.BooleanField(verbose_name = u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'socservice')
        verbose_name_plural = _(u'socservices')

    def get_absolute_url(self):
        return u'/socialservices/%s/' % self.id

class Purchase(models.Model):
    title = models.CharField(max_length=120, verbose_name=u'название')
    short_description =  models.TextField(verbose_name = u'краткое описание')
    description =  models.TextField(verbose_name = u'полное описание')
    url = models.URLField(verify_exists=False, verbose_name=u'ссылка на сайт госзакупок', help_text=u'Адрес на латинице. Например, "http://your_address/"')
    protocol_file = models.FileField(upload_to='PurchasesProtocols/', verbose_name=u'файл протокола', blank=True)
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)
    is_published = models.BooleanField(verbose_name = u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'purchase')
        verbose_name_plural = _(u'purchases')

    def get_absolute_url(self):
        return u'/purchases/%s/' % self.id

    def get_file_path(self):
        return self.protocol_file.url

    def get_fmt_ext(self):
        extension = os.path.splitext(self.protocol_file.name)[1]
        extension = extension[1:]
        if extension in [u'pdf',u'doc',u'txt']:
            return u'fmt_%s' % extension
        else:
            return u'fmt_any'

class ImageField(models.ImageField, sorl_ImageField):
    pass

def image_path_adminPhoto(instance, filename):
    return os.path.join('images','admin_persons', translify(filename).replace(' ', '_') )

class AdminPerson(models.Model):
    fullname = models.CharField(max_length = 150, verbose_name = u'полное имя')
    post_title = models.CharField(max_length = 255, verbose_name = u'должность')
    photo = ImageField(upload_to=image_path_adminPhoto, verbose_name=u'фотография')
    phone_num = models.CharField(max_length = 50, verbose_name = u'телефонный номер')
    office_hours = models.CharField(max_length = 150, verbose_name = u'часы приёма')
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)
    is_published = models.BooleanField(verbose_name = u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return self.fullname

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'adminperson')
        verbose_name_plural = _(u'adminpersons')

    def get_src_photo(self):
        return self.photo.url