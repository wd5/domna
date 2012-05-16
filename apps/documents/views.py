# -*- coding: utf-8 -*-

from django.views.generic import ListView, CreateView, DetailView
from apps.documents.models import DocumentCategory,Document

class DocumentListDetailView(DetailView):
    model = DocumentCategory
    template_name = 'documents/documents_list.html'
    context_object_name = 'docCateg'

    def get_context_data(self, **kwargs):
        context = super(DocumentListDetailView, self).get_context_data(**kwargs)

        childcat = context['docCateg'].get_children().filter(is_published = True)
        context['childcat'] = childcat
        try:
            documents = Document.objects.published().filter(documentcategory__in=context['childcat'])
        except Document.DoesNotExist:
            documents = False
        context['generaldocs'] = documents

        return context

documents_list = DocumentListDetailView.as_view()

class DocumentListByCatDetailView(DetailView):
    model = DocumentCategory
    template_name = 'documents/documents_list.html'
    context_object_name = 'subCateg'

    def get_context_data(self, **kwargs):
        context = super(DocumentListByCatDetailView, self).get_context_data(**kwargs)

        parentcat = context['subCateg'].parent
        childcat = parentcat.get_children().filter(is_published = True)
        context['docCateg'] = parentcat
        context['childcat'] = childcat
        context['generaldocs'] = context['subCateg'].get_documents()

        return context

documents_list_by_categ = DocumentListByCatDetailView.as_view()