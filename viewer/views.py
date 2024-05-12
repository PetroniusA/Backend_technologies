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

def hello4(request):
   adjectives = ['nice' , 'beautiful' , 'cruel' , 'blue' , 'sunny']
   context = {'adjectives' : adjectives}
   return render(
       request,
       template_name='hello.html',
       context=context,
   )

def hello5(request, s0):
        s1 = request.GET.get('s1', '')
        return render(
        request, template_name='hello.html',
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful']}
       )

