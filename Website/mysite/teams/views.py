from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Team

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render(request))