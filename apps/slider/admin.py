# -*- coding: utf-8 -*-
from django.contrib import admin

from apps.slider.models import Photo
from sorl.thumbnail.admin import AdminImageMixin

class PhotoAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('id','admin_photo_preview','order','show',)
    list_display_links = ('id','admin_photo_preview',)
    list_editable = ('order','show',)
    list_filter = ('show',)

admin.site.register(Photo, PhotoAdmin)