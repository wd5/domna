# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url

#from apps.app.urls import urlpatterns as app_url

urlpatterns = patterns('',

    url(r'^$', 'apps.views.index'),

    url(r'^faq/$','apps.faq.views.questions_list'),
    url(r'^faq/sendquestion/$','apps.faq.views.question_form'),
    url(r'^faq/checkform/$','apps.faq.views.checkqform'),

    url(r'^council/$', 'apps.council.views.council_list'),
    url(r'^council/(?P<pk>[^/]+)/$', 'apps.council.views.show_council_item'),

    url(r'^documents/$', 'apps.documents.views.documents_list', {'pk':'1'}),
    url(r'^documents/(?P<pk>[^/]+)/$', 'apps.documents.views.documents_list'),
    url(r'^documents/[^/]+/(?P<pk>[^/]+)/$', 'apps.documents.views.documents_list_by_categ'),

    url(r'^socialservices/$', 'apps.social.views.socserv_list'),
    url(r'^socialservices/(?P<pk>[^/]+)/$', 'apps.social.views.show_socserv'),

    url(r'^purchases/$', 'apps.social.views.purchases_list'),
    url(r'^purchases/(?P<pk>[^/]+)/$', 'apps.social.views.show_purchase'),

    url(r'^administration/$', 'apps.social.views.administration_list'),

    url(r'^news/$', 'apps.newsboard.views.news_list'),
    url(r'^news/(?P<pk>[^/]+)/$', 'apps.newsboard.views.news_detail'),

)


