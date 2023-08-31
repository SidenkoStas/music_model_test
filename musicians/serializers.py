from rest_framework import serializers
from .models import Musician, Album, Song, SongAlbumRelationship


class MusicianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Musician
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = Album
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    albums = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(queryset=Album.objects.all()),
        write_only=True
    )

    class Meta:
        model = Song
        fields = "__all__"

    def create(self, validated_data):
        albums = validated_data.pop("albums", [])
        song = Song.objects.create(**validated_data)
        for album in albums:
            SongAlbumRelationship.objects.create(song=song, album=album)
        return song


class SongAlbumRelationshipSerializer(serializers.ModelSerializer):

    class Meta:
        model = SongAlbumRelationship
        fields = "__all__"
