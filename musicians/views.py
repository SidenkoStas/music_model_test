from .models import Musician, Album, Song, SongAlbumRelationship
from .serializers import (MusicianSerializer, AlbumSerializer, SongSerializer,
                          SongAlbumRelationshipSerializer)
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiExample


class MusicianViewSet(ModelViewSet):
    """
    Представление для работы с моделью Musicia.
    """
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
    @extend_schema(
        examples=[
            OpenApiExample(
                "Пример",
                value={
                    "musician": {
                        "id": 1,
                        "name": "string"
                    },
                    "albums": [
                        {
                            "id": 1,
                            "title": "string",
                            "year": 0000,
                            "musician": 1
                        },
                    ],
                    "songs": [
                        {
                            "id": 1,
                            "title": "string"
                        },
                    ]
                },
            )
        ]
    )
    def retrieve(self, request, *args, **kwargs):
        """
        При запросе профиля музыканта, выдаёт список альбомов и все песни для
        данного музыканта(только для чтения).
        """
        musician = Musician.objects.get(pk=kwargs["pk"])
        songs = Song.objects.filter(albums__musician=kwargs["pk"])
        albums = Album.objects.filter(musician=kwargs["pk"])
        serializer_musician = MusicianSerializer(musician)
        serializer_songs = SongSerializer(songs, many=True, read_only=True)
        serializer_albums = AlbumSerializer(albums, many=True, read_only=True)
        return Response({"musician": serializer_musician.data,
                         "albums": serializer_albums.data,
                         "songs": serializer_songs.data})


class AlbumViewSet(ModelViewSet):
    """
    Представление для работы с моделью Album.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    @extend_schema(
        examples=[
            OpenApiExample(
                "Пример",
                value={
                    "albums": {
                        "id": 1,
                        "title": "string",
                        "year": 0000,
                        "musician": 1
                    },
                    "songs": [
                        {
                            "id": 0,
                            "title": "string"
                        },
                    ]
                },
            )
        ]
    )
    def retrieve(self, request, *args, **kwargs):
        """
        При запросе деталей альбома, выдаёт список песен для
        данного альбома(только для чтения).
        """
        album = Album.objects.get(pk=kwargs["pk"])
        songs = Song.objects.filter(albums=kwargs["pk"])
        serializer_albums = AlbumSerializer(album)
        serializer_songs = SongSerializer(songs, many=True, read_only=True)
        return Response({"albums": serializer_albums.data,
                         "songs": serializer_songs.data})


class SongViewSet(ModelViewSet):
    """
    Представление для работы с моделью Song.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    @extend_schema(
        examples=[
            OpenApiExample(
                "Пример",
                value={
                    "song": {
                        "id": 1,
                        "title": "string"
                    },
                    "relations": [
                        {
                            "id": 1,
                            "track_number": 1,
                            "song": 1,
                            "album": 1
                        },
                    ]
                }
            )
        ]
    )
    def retrieve(self, request, *args, **kwargs):
        """
        При запросе деталей песни, выдаёт список альбомов и номера в
         этих альбомах.
        """
        relations = SongAlbumRelationship.objects.filter(song=kwargs["pk"])
        song = Song.objects.get(pk=kwargs["pk"])
        serializer_relations = SongAlbumRelationshipSerializer(relations,
                                                               many=True)
        serializer_song = SongSerializer(song)
        return Response({"song": serializer_song.data,
                         "relations": serializer_relations.data})
