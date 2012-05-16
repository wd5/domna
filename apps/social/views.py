# -*- coding: utf-8 -*-

from django.views.generic import ListView, CreateView, DetailView
from apps.social.models import SocialService,Purchase,AdminPerson

class SocialServListView(ListView):
    model = SocialService
    template_name = 'social/socserv_block.html'
    context_object_name = 'socservices'

    def get_context_data(self, **kwargs):
        context = super(SocialServListView, self).get_context_data(**kwargs)
        context['socservices'] = context['socservices'].published()
        return context

socserv_list = SocialServListView.as_view()

class ShowSocServView(DetailView):
    model = SocialService
    template_name = 'social/socserv_block.html'
    context_object_name = 'service'

    def get_context_data(self, **kwargs):
        context = super(ShowSocServView, self).get_context_data(**kwargs)

        if context['service'].is_published == False:
            context['service'] = False

        return context

show_socserv = ShowSocServView.as_view()

class PurchaseListView(ListView):
    model = Purchase
    template_name = 'social/purchases_block.html'
    context_object_name = 'purchases'

    def get_context_data(self, **kwargs):
        context = super(PurchaseListView, self).get_context_data(**kwargs)
        context['purchases'] = context['purchases'].published()
        return context

purchases_list = PurchaseListView.as_view()

class ShowPurchaseView(DetailView):
    model = Purchase
    template_name = 'social/purchases_block.html'
    context_object_name = 'purchase'

    def get_context_data(self, **kwargs):
        context = super(ShowPurchaseView, self).get_context_data(**kwargs)

        if context['purchase'].is_published == False:
            context['purchase'] = False

        return context

show_purchase = ShowPurchaseView.as_view()

class AdministrationListView(ListView):
    model = AdminPerson
    template_name = 'social/administration_list.html'
    context_object_name = 'persons'

    def get_context_data(self, **kwargs):
        context = super(AdministrationListView, self).get_context_data(**kwargs)
        context['persons'] = context['persons'].published()
        return context

administration_list = AdministrationListView.as_view()


