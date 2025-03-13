from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Movie

def home(request):
    template = loader.get_template('home.html')
    context = {
        'movies' : Movie.objects.all()
    }
    return HttpResponse(template.render(context, request))