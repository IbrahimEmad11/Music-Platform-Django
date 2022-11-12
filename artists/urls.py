from django.urls import path
from . import views
from .views import ArtistList



urlpatterns=[
    path('' , ArtistList.as_view(), name='artists'),
    ]