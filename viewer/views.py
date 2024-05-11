from django.http import HttpResponse
from django.shortcuts import render

# view defined using function

def hello(request):
    return HttpResponse("Hello world")

def hello2(request, str):
    return HttpResponse(f'Hello {str} world')

def hello3(request):
    s = request.GET.get("str" , "")
    return HttpResponse(f'Hello , {s}, world')

