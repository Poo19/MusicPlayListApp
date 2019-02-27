from django.db import models
import datetime

# Create your models here.
class Genre(models.Model):
    name  = models.CharField(max_length=120,unique=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name


class Artist(models.Model):
    name  = models.CharField(max_length=120,unique=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Song(models.Model):
    artist = models.ForeignKey(Artist)
    genre = models.ForeignKey(Genre)
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(default=datetime.date.today, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    # duration in minutes
    duration =  models.DurationField( default=datetime.timedelta)

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ["title", "artist"],
        index_together = ["title", "artist"]
