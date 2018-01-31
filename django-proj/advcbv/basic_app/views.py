from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View, TemplateView
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from . import models

#class CBView(View):
#    def get(self, request):
#        return HttpResponse("This is a class based view")

# class CBTemplateView(TemplateView):
#    template_name = 'index.html'
#
#    def get_context_data(self, **kwargs):
#            context = super().get_context_data(**kwargs)
#            context['injectme'] = 'Injection context'
#            return context

class SchoolListView(ListView):
    model = models.School
    context_object_name = 'schools'

class SchoolDetailView(DetailView):
    model = models.School
    template_name = 'basic_app/school_detail.html'

class IndexView(TemplateView):
    template_name = 'index.html'

class SchoolCreateView(CreateView):
    fields = ("name","principal","location")
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ("name","principal")
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")


class CBView(View):
    def get(self,request):
        return HttpResponse('Class Based Views are Cool!')
