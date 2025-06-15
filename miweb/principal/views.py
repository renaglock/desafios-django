from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    contexto = {'nombre': 'Usuario'}
    return render(request, 'index.html', contexto)

def saludo(request):
    return HttpResponse("¡Hola, desde mi vista de Django!")

def saludar_usuario(request, nombre):
    return HttpResponse(f"Hola, {nombre}!")

def edad(request, edad):
    return HttpResponse(f"Hola, tienes {edad} años!")
