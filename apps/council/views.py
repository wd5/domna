# -*- coding: utf-8 -*-

from django.views.generic import ListView, CreateView, DetailView
from apps.council.models import CouncilItem

class CouncilListView(ListView):
    model = CouncilItem
    template_name = 'council/council_block.html'
    context_object_name = 'CouncilItems'

    def get_context_data(self, **kwargs):
        context = super(CouncilListView, self).get_context_data(**kwargs)
        context['CouncilItems'] = context['CouncilItems'].published()
        return context

council_list = CouncilListView.as_view()

class ShowCouncilView(DetailView):
    model = CouncilItem
    template_name = 'council/council_block.html'
    context_object_name = 'council_item'

    def get_context_data(self, **kwargs):
        context = super(ShowCouncilView, self).get_context_data(**kwargs)

        if context['council_item'].is_published == False:
            context['council_item'] = False

        return context

show_council_item = ShowCouncilView.as_view()