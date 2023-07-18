from django.urls import path
from .views import HomeView, Press_releaseView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', HomeView.as_view(), name="home"),
    path('press', Press_releaseView.as_view(), name='press')

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
