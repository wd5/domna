# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from apps.council.models import CouncilItem,Attached_doc
from apps.utils.widgets import Redactor

class AttachedDocInline(admin.TabularInline):
    model = Attached_doc

class CouncilItemAdminForm(forms.ModelForm):
    description = forms.CharField(
        widget=Redactor(attrs={'cols': 170, 'rows': 20}),
        label = u'Полное описание',
    )
    class Meta:
        model = CouncilItem

class CouncilItemAdmin(admin.ModelAdmin):
    list_display = ('id','short_description','date_add','is_published',)
    list_display_links = ('id','short_description',)
    list_editable = ('is_published',)
    search_fields = ('short_description','description')
    list_filter = ('date_add','is_published',)
    inlines = [AttachedDocInline]
    form = CouncilItemAdminForm

admin.site.register(CouncilItem, CouncilItemAdmin)
