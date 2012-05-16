# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
import os
from django.db import models
from sorl.thumbnail.fields import ImageField
from pytils.translit import translify
from apps.utils.models import BaseDoc, BasePic
from apps.utils.managers import PublishedManager

class Page(models.Model):
    date_add = models.DateTimeField(verbose_name=u'Дата создания', editable=False, auto_now_add=True)
    title = models.CharField(max_length=120, verbose_name=u'Заголовок страницы', blank=True)
    url = models.CharField(max_length=200, verbose_name=u'Адрес', unique=True, help_text=u'Адрес страницы на латинице. Например, "/your_address/"')
    content = models.TextField(verbose_name=u'Содержимое страницы')
    order = models.IntegerField(verbose_name=u'Порядок сортировки',default=10)

    is_published = models.BooleanField(verbose_name=u'Опубликовано', default = True)
    template = models.CharField(verbose_name=u'шаблон', max_length=100, editable=False, default=u'default.html')

    objects = PublishedManager()

    def get_absolute_url(self):
        return self.url

    class Meta:
        verbose_name = _(u'page_item')
        verbose_name_plural = _(u'page_items')

    def __unicode__(self):
        return u'%s (%s)' % (self.title, self.get_absolute_url())

    def get_attached_photos(self):
        return self.pageattachedphoto_set.all()

    def save(self, **kwargs):
        # add the first and the last slash if it needed
        if not self.url.endswith('/'):
            self.url += '/'
        if not self.url.startswith('/'):
            self.url = "/" + self.url

        # remove the first and the last space
        self.title = self.title.strip()
 
        super(Page, self).save(**kwargs)

def image_path_AttachedPhoto(instance, filename):
    return os.path.join('images','page_photos', translify(filename).replace(' ', '_') )

class PageAttachedPhoto(models.Model):
    page = models.ForeignKey(Page, verbose_name=u'страница')
    image = ImageField(upload_to=image_path_AttachedPhoto, verbose_name=u'изображение')
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)

    def __unicode__(self):
        return u'фотография для страницы "%s" ' % self.page.title

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'attached_photo')
        verbose_name_plural = _(u'attached_photos')

    def get_src_image(self):
        return self.image.url


class PageDoc(BaseDoc):
    page = models.ForeignKey(
        Page,
        verbose_name = u'страница',
    )

    class Meta:
        verbose_name = u'файл'
        verbose_name_plural = u'файлы'

    def __unicode__(self):
        return u'%s' % self.title

    def get_upload_path(self, filename):
        return os.path.join('files', 'page_docs')

class PagePic(BasePic):
    page = models.ForeignKey(
        Page,
        verbose_name = u'страница',
    )

    class Meta:
        verbose_name = u'картинка'
        verbose_name_plural = u'картинки'

    def __unicode__(self):
        return u'%s' % self.title

    def get_upload_path(self, filename):
        return os.path.join('files', 'page_pics')


class MetaData(models.Model):
    url = models.CharField(max_length=100, verbose_name=u'Адрес', help_text=u'Адрес страницы,например, "/your_address/"')
    title = models.CharField(max_length=100, verbose_name=u'Заголовок')
    description = models.CharField(max_length=100, verbose_name=u'description', blank=True)
    keywords = models.CharField(max_length=100, verbose_name=u'keywords', blank=True)

    class Meta:
        verbose_name = u'meta'
        verbose_name_plural = u'meta'

    def __unicode__(self):
        return u'%s| %s' % (self.url, self.title)


    def save(self, force_insert=False, force_update=False, using=None):
        # add the first and the last slash if it needed
        if not self.url.endswith('/'):
            self.url += '/'
        if not self.url.startswith('/'):
            self.url = '/' + self.url

        if force_insert and force_update:
            raise ValueError("Cannot force both insert and updating in model saving.")
        self.save_base(using=using, force_insert=force_insert, force_update=force_update)

    save.alters_data = True