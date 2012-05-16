# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from mptt.admin import MPTTModelAdmin
from apps.documents.models import Document,DocumentCategory
from sorl.thumbnail.admin import AdminImageMixin

class DocumentAdminForm(forms.ModelForm):
    documentcategory = forms.ModelChoiceField(queryset=DocumentCategory.objects.exclude(parent=None), label='Категория')
    class Meta:
        model = Document

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id','title','documentcategory','order','is_published',)
    list_display_links = ('id','title',)
    list_editable = ('order','is_published',)
    search_fields = ('title',)
    list_filter = ('documentcategory','is_published',)
    #raw_id_fields = ('documentcategory',)
    form = DocumentAdminForm

class DocumentCategoryAdminForm(forms.ModelForm):
    parent = forms.ModelChoiceField(queryset=DocumentCategory.objects.filter(parent=None), label='Родительская категория', required=True)
    class Meta:
        model = DocumentCategory

class DocumentCategoryAdmin(MPTTModelAdmin):
    list_display = ('id','title','order','is_published',)
    list_display_links = ('id','title',)
    list_editable = ('order','is_published',)
    search_fields = ('title',)
    list_filter = ('parent','is_published',)
    list_select_related = True
    form = DocumentCategoryAdminForm

admin.site.register(Document, DocumentAdmin)
admin.site.register(DocumentCategory, DocumentCategoryAdmin)