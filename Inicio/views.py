from django.shortcuts import render
from rest_framework import viewsets
#from .serializers import PersonaSerializers
#from .models import Persona
from django.http import HttpResponse
# Create your views here.
def homepage(request):
    return HttpResponse('<h1>HOLA</h1>')

