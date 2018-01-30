from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView
from . import models

#class CBView(View):
#    def get(self, request):
#        return HttpResponse("This is a class based view")

class CBTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['injectme'] = 'Injection context'
            return context

class SchoolListView(ListView):
    model = models.School
    context_object_name = 'school'

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'

class IndexView(TemplateView):
    template_name = 'index.html'
