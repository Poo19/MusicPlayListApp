from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )

from accounts.api.serializers import UserDetailSerializer
from playlists.models import Playlist
from songs.api.serializers import SongListSerializer

class PlayListSerializer(ModelSerializer):
    songs =  SongListSerializer(many=True, read_only=True)
    user = UserDetailSerializer()
    class Meta:
        model = Playlist
        fields = [
            'user',
            'songs',
            'title',
            'slug', 
            'access' 
        ]

class PlayListCreateUpdateSerializer(ModelSerializer):
    songs =  SongListSerializer(many=True, read_only=True)
    class Meta:
        model = Playlist
        fields = [
            'songs',
            'title',
            'slug', 
            'access' 
    ]
