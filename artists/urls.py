from django.urls import path

from . import views

from artists.views import ArtistList

urlpatterns=[
    path('' , ArtistList.as_view(), name='artist_list'),
    path('create/' , views.create_artist , name='create')
]