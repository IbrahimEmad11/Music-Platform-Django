from django.urls import path

from . import views

from .views import AlbumView,SongView



urlpatterns=[
    path('create/' , AlbumView.as_view() , name='create'),
    path('song/' , SongView.as_view() , name='song'),
]