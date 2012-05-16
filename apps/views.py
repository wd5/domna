# -*- coding: utf-8 -*-
#from django.template import loader, RequestContext, Context
from apps.siteblocks.models import Settings
from apps.documents.models import Document, DocumentCategory
from apps.siteblocks.models import SiteMenu
from apps.social.models import SocialService
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data()
        try:
            shortabout = Settings.objects.get(name='shortabout').value
        except Settings.DoesNotExist:
            shortabout = False
        try:
            dscategory = DocumentCategory.objects.get(id='1')

        except DocumentCategory.DoesNotExist:
            dscategory = False

        if dscategory:
            childcat = dscategory.get_children()
            childcat = childcat.filter(is_published = True)
            try:
                documents = Document.objects.published().filter(documentcategory__in=childcat)
            except Document.DoesNotExist:
                documents = False
        else:
            documents = False

        try:
            sstitle = SiteMenu.objects.get(id=3)
        except:
            sstitle = False

        try:
            socialservset = SocialService.objects.published()
        except:
            socialservset = False

        context['shortabout'] = shortabout
        context['dscategory'] = dscategory
        context['documents'] = documents
        context['sstitle'] = sstitle
        context['socialservset'] = socialservset
        return context

index = Index.as_view()