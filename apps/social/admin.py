# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from apps.social.models import AdminPerson,Purchase,SocialService
from apps.utils.widgets import Redactor, AdminImageWidget
from sorl.thumbnail.admin import AdminImageMixin

class AdminPersonAdmin(AdminImageMixin,admin.ModelAdmin):
    list_display = ('id','fullname','post_title','order','is_published',)
    list_display_links = ('id','fullname','post_title',)
    list_editable = ('is_published','order',)
    search_fields = ('fullname','post_title','phone_num','office_hours',)
    list_filter = ('is_published',)

class PurchaseAdminForm(forms.ModelForm):
    description = forms.CharField(
        widget=Redactor(attrs={'cols': 170, 'rows': 20}),
        label = u'Полное описание',
    )
    class Meta:
        model = Purchase

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id','title','order','is_published',)
    list_display_links = ('id','title',)
    list_editable = ('is_published','order',)
    search_fields = ('title','short_description','description',)
    list_filter = ('is_published',)
    form = PurchaseAdminForm

class SocialServiceAdminForm(forms.ModelForm):
    description = forms.CharField(
        widget=Redactor(attrs={'cols': 170, 'rows': 20}),
        label = u'Описание услуги',
    )
    class Meta:
        model = SocialService

class SocialServiceAdmin(admin.ModelAdmin):
    list_display = ('id','title','order','is_published',)
    list_display_links = ('id','title',)
    list_editable = ('is_published','order',)
    search_fields = ('title','description',)
    list_filter = ('is_published',)
    form = SocialServiceAdminForm


admin.site.register(AdminPerson, AdminPersonAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(SocialService, SocialServiceAdmin)