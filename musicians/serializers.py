from rest_framework import serializers
from .models import Musician, Album, Song, SongAlbumRelationship


class MusicianSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с моделью Musician.
    """
    class Meta:
        model = Musician
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с моделью Album.
    """
    class Meta:
        model = Album
        fields = "__all__"


class SongSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с моделью Song.
    """
    albums = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(queryset=Album.objects.all()),
        write_only=True
    )

    class Meta:
        model = Song
        fields = "__all__"

    def create(self, validated_data):
        """
        Создаёт запись о песне и прописывает связь песни с указанными альбомами
        в промежуточной таблице SongAlbumRelationship.
        """
        albums = validated_data.pop("albums", [])
        song = Song.objects.create(**validated_data)
        for album in albums:
            SongAlbumRelationship.objects.create(song=song, album=album)
        return song


class SongAlbumRelationshipSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с моделью SongAlbumRelationship - промежуточной
     моделью отношения many_to_many моделей Song и  Album.
    """
    class Meta:
        model = SongAlbumRelationship
        fields = "__all__"
