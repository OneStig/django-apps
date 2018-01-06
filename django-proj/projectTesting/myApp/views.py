from django.shortcuts import render

# Create your views here.
def index(request):
    mdictionary = {'insert_content':"From firstapp"}
    return render(request, 'myApp/index.html', context=mdictionary)
