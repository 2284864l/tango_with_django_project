from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def homepage(requeest):
    return HttpResponse("Homepage"
                        "<br>"
                        "<a href='/rango/'>Index</href>"
                        "<br>"
                        "<a href='/rango/about/'>About</href>")

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dict = {'author': "SHENGXIAN LIU: 2284864L"}
    return render(request, 'rango/about.html', context=context_dict)
