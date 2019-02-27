import csv
import datetime
import calendar
import django, os,sys
os.chdir(sys.path[0])


from django.template.loader import get_template
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "musicapp.settings.base")
django.setup()

from songs.models import Song,Artist,Genre
with open("topSongs2018.csv", 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        eachRowDict = dict(row)
        #eachRowDict['date'] = datetime.date(2018, 1, 1)

        artist, created = Artist.objects.get_or_create(
            name = eachRowDict['artists']
        )
        
        genre = Genre.objects.get(
            name__icontains ='pop'
        )
        duration_ms =  datetime.timedelta(milliseconds = int(eachRowDict['duration_ms']))
       
        if artist and genre:
            if not Song.objects.filter(slug = eachRowDict['id'] ).exists():
                song = Song.objects.create(
                    title = eachRowDict['name'],
                    artist = artist,
                    genre = genre,
                    slug = eachRowDict['id'],
                    date = datetime.date(2018, 1, 1),
                    duration = duration_ms
                )  



