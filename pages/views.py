from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse

def index(request):
    args = {}
    fruits_list = ["apple", "banana", "mango"]
    fruits_list.append("orange")
    fruits_list.append("grapes")
    args['fruits_list'] = fruits_list
    #return render(request, 'pages/index.html')
    return TemplateResponse(request, 'pages/index.html', args)

def about(request):
    return render(request, 'pages/about.html')
