from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, idade):
    return HttpResponse(f'<H1>Hello {nome} de {idade} anos<H1>')
