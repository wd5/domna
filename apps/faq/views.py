# -*- coding: utf-8 -*-
import datetime
from django.http import HttpResponse,HttpResponseBadRequest
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView,FormView
from apps.faq.forms import QuestionForm
from apps.faq.models import Question

class QuestionListView(TemplateView):
    template_name = 'faq/faq.html'

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        context['questions'] = Question.objects.published()
        return context

questions_list = QuestionListView.as_view()

class FaqFormView(FormView):
    form_class = QuestionForm
    template_name = 'faq/faq_form.html'

question_form = FaqFormView.as_view()

@csrf_exempt
def checkqform(request):
    if request.is_ajax():
        data = request.POST.copy()
        faq_form = QuestionForm(data)
        if faq_form.is_valid():
            faq_form.save()
            return HttpResponse('success')
        else:
            faq_form_html = render_to_string(
                'faq/faq_form.html',
                    {'form': faq_form}
            )
            return HttpResponse(faq_form_html)
    else:
        return HttpResponseBadRequest()