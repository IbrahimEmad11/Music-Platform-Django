from django.urls import path

from . import views

from .views import AlbumView,SongView,AlbumList,AlbumListManual



urlpatterns=[
    path('create/' , AlbumView.as_view() , name='create'),
    path('song/' , SongView.as_view() , name='song'),
    path('', AlbumList.as_view(),name='album_list'),
    path('manual/',AlbumListManual.as_view(),name='album_list_manual')
]