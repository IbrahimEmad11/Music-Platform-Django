from django.urls import path
from . import views
from .views import LoginPageView
# from .views import ArtistList,ArtistForm, ArtistView



urlpatterns=[
    path('' , LoginPageView.as_view(), name='login'),
    
]