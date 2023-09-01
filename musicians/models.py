from django.db import models


class Musician(models.Model):
    """
    Модель музыкальных исполнителей.
    """
    name = models.CharField(max_length=255, verbose_name="Музыкант")

    def __str__(self):
        return f"{self.name}"


class Album(models.Model):
    """
    Модель альбомов.
    """
    title = models.CharField(max_length=255, verbose_name="Название")
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE,
                                 related_name="albums",
                                 verbose_name="Музыкант")
    year = models.PositiveIntegerField(verbose_name="Год альбома")

    def __str__(self):
        return f"{self.musician} - {self.title} - {self.year}"


class Song(models.Model):
    """
    Модель песен.
    """
    title = models.CharField(max_length=255, verbose_name="Название")
    albums = models.ManyToManyField(Album, through='SongAlbumRelationship',
                                    related_name="songs")

    def __str__(self):
        return f"{self.title}"


class SongAlbumRelationship(models.Model):
    """
    Промежуточная модель для many_to_many Song & Album.
    """
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    track_number = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['song', "track_number", 'album'],
                                    name='unique_song_in_album')
        ]

    def __str__(self):
        return f"'{self.song}' - '{self.album}' - {self.track_number}"

    def save(self, *args, **kwargs):
        """
        При сохранении автоматически присваивает номер трека в альбомк, исходя
        из максимального значения или отсутствующего значения, если ранеее
        какой-то трек был удалён из альбома.
        """
        album_songs = SongAlbumRelationship.objects.filter(
            album=self.album)
        max_track_number = album_songs.aggregate(
            models.Max('track_number')
        )['track_number__max']
        if max_track_number is None:
            self.track_number = 1
        elif max_track_number == album_songs.count():
            self.track_number = max_track_number + 1
        else:
            all_tracks_num = album_songs.values_list("track_number", flat=True)
            for i in range(1, max_track_number+1):
                if i != all_tracks_num[i-1]:
                    self.track_number = i
                    break
        super().save(*args, **kwargs)
