# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# from .models import SongAlbumRelationship
# from django.db.models import Max
#
#
# @receiver(pre_save, sender=SongAlbumRelationship)
# def set_track_number(sender, instance, **kwargs):
#     """
#     Испоьзование сигнала для автоматического назначения поля track_number перед
#     сохранением модели.
#     """
#     existing_songs = SongAlbumRelationship.objects.filter(album=instance.album)
#     max_track_number = existing_songs.aggregate(
#         Max('track_number')
#     )['track_number__max']
#     instance.track_number = max_track_number + 1 \
#         if max_track_number is not None else 1
