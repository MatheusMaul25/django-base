# from django.http import HttpResponse


# def home(request):
#     print('home')
#     return HttpResponse('home do app 2')

from django.shortcuts import render

def home(request):

    context = {
        'text': 'Estamos na home',
        'title': 'Home',
        }

    return render(
        request, 
        'home/index.html',
        context,
        )