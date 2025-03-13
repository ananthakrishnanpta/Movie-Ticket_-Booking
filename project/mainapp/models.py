from django.db import models

# Create your models here.

movie_category = {
    'action': 'Action',
    'comedy': 'Comedy',
    'drama': 'Drama',
    'horror': 'Horror',
    'romance': 'Romance',
    'thriller': 'Thriller',
    'sci-fi': 'Science Fiction',
    'documentary': 'Documentary',
    'animation': 'Animation',
    'fantasy': 'Fantasy',
}

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(choices=movie_category, null=False, max_length=25)
