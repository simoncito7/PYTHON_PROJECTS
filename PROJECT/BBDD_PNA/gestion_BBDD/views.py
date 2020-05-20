from django.shortcuts import render, HttpResponse

# Create your views here.

# acá creamos tantas vistas (funciones) como páginas manejemos.

def causas(request):

    return HttpResponse("Causas")


def numerador(request):

    return HttpResponse("Numerador")
