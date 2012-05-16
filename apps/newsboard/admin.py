# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from apps.utils.widgets import Redactor
from models import News

class NewsAdminForm(forms.ModelForm):
    text = forms.CharField(
        widget=Redactor(attrs={'cols': 170, 'rows': 30}),
        label = u'Текст новости',
    )
    class Meta:
        model = News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','short_text', 'date_add', 'is_published',)
    list_display_links = ('short_text',)
    list_filter = ('is_published',)
    list_editable = ('is_published',)
    form = NewsAdminForm
    date_hierarchy = 'date_add'

admin.site.register(News, NewsAdmin)
