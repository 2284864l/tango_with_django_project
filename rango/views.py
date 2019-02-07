from django.shortcuts import render
from django.http import HttpResponse

def homepage(requeest):
    return HttpResponse("Homepage"
                        "<br>"
                        "<a href='/rango/'>Index</href>"
                        "<br>"
                        "<a href='/rango/about'>About</href>")

def index(request):
    return HttpResponse("Rango says hey there partner!"
                        "<br>"
                        "<a href='/rango/about'>About</href>")

def about(request):
    return HttpResponse("rango says here is the about page"
                        "<br/>"
                        "<a href='/rango/'>Index</href>") 
