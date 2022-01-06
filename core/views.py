from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome, idade):
    return HttpResponse(f'<H1>Hello {nome} de {idade} anos<H1>')


def soma(request, vlr1, vlr2):
    return HttpResponse(int(vlr1) + int(vlr2))
