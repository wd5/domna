# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from datetime import date, datetime, timedelta
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.syndication.views import Feed
from django.shortcuts import get_object_or_404
from django import http
from apps.newsboard.models import News

class NewsListView(ListView):
    model = News
    template_name = 'newsboard/news_page.html'

    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['news_list'] = context['news_list'].published()
        return context

news_list = NewsListView.as_view()

class NewsDetailView(DetailView):
    context_object_name = 'news_current'
    model = News
    template_name = 'newsboard/news_page.html'

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        if context['news_current'].is_published == False:
            context['news_current'] = False
        return context

news_detail = NewsDetailView.as_view()

class LatestNewsFeed(Feed):
    title = _(u'Новости')
    link = '/news/'
    description = ''

    def items(self):
        return News.objects.published()[:50]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.short_text