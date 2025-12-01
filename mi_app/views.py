from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return HttpResponse("Hola Django!")

def index(request):
   return render(request, 'mi_app/index.html')