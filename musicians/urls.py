from rest_framework.routers import DefaultRouter
from .views import MusicianViewSet, AlbumViewSet, SongViewSet


app_name = "musicians"

router = DefaultRouter()
router.register(r"musicians", MusicianViewSet)
router.register(r"albums", AlbumViewSet)
router.register(r"songs", SongViewSet)
urlpatterns = router.urls
