from django.urls import path
from . import views
from .views import ArtistList,ArtistForm, ArtistView



urlpatterns=[
    path('' , ArtistList.as_view(), name='artists'),
    path('create/' , ArtistView.as_view() , name='create')
]