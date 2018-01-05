from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    dictionary = {'insert_me':"This is inserted from views.py"}
    return render(request, 'index.html', context=dictionary)
