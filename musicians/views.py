from rest_framework import status

from .models import Musician, Album, Song, SongAlbumRelationship
from .serializers import (MusicianSerializer, AlbumSerializer, SongSerializer,
                          SongAlbumRelationshipSerializer)
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response


class MusicianViewSet(ModelViewSet):
    """
    Обработчик для модели Musicia.
    """
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer

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
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

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
    queryset = Song.objects.all()
    serializer_class = SongSerializer

    # def create(self, request, *args, **kwargs):
    #     albums = request.data.pop('albums', [])
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #
    #     instance = serializer.instance
    #     instance.albums.set(albums)
    #
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED,
    #                     headers=headers)

    def retrieve(self, request, *args, **kwargs):
        """
        При запросе деталей песни, выдаёт список альбомов и номера в
         этих альбомах(только для чтения).
        """
        relations = SongAlbumRelationship.objects.filter(song=kwargs["pk"])
        song = Song.objects.get(pk=kwargs["pk"])
        serializer_relations = SongAlbumRelationshipSerializer(relations,
                                                               many=True)
        serializer_song = SongSerializer(song)
        return Response({"song": serializer_song.data,
                        "relations": serializer_relations.data})
