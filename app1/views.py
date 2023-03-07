from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def game(request):
    return HttpResponse('<h2> This is first app</h2>')

def tom(request):
    return HttpResponse('<marquee><h1> Tom and Jerry are Friends</h1>')
    


