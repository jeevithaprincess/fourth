from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def chotta(request):
    return HttpResponse('<h2> Chotta Bheema is pogo channel</h2')

def micky(request):
    return HttpResponse('<marquee><h1>micky mouse is cartoon channel</h1>')
    
