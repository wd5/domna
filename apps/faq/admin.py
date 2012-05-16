# -*- coding: utf-8 -*-
from django.contrib import admin
from apps.faq.models import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','pub_date','is_published',)
    list_display_links = ('id','pub_date',)
    list_editable = ('is_published',)
    search_fields = ('question', 'answer',)
    list_filter = ('pub_date','is_published',)

admin.site.register(Question, QuestionAdmin)