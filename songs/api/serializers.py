from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )

from songs.models import Song,Artist,Genre

class SongListSerializer(ModelSerializer):
    artist = SerializerMethodField()
    duration = SerializerMethodField()
    genre =  SerializerMethodField()
    year = SerializerMethodField()
    class Meta:
        model = Song
        fields = [
            'artist',
            'genre',
            'title',
            'slug', 
            'date',
            'duration',
            'year'
        ]
    
    def get_artist(self, obj):
        return obj.artist.name

    def get_genre(self, obj):
        return obj.genre.name

    def get_duration(self, obj):
        minutes = int(obj.duration.seconds) / 60
        return str("{0:.2f}".format(round(minutes,2)))

    def get_year(self, obj):
        return str(obj.date.year)

