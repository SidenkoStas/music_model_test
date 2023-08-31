from django.contrib import admin
from .models import Album, Musician, Song, SongAlbumRelationship


class SongAlbumRelationshipInline(admin.TabularInline):
    model = SongAlbumRelationship
    extra = 1


class SongAdmin(admin.ModelAdmin):
    model = Song
    inlines = [SongAlbumRelationshipInline]


admin.site.register(Album)
admin.site.register(Musician)
admin.site.register(Song, SongAdmin)
admin.site.register(SongAlbumRelationship)
