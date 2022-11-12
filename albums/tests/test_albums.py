
from users.models import User
from artists.models import Artist
from ..models import Album
from ..serializers import AlbumSerializer
import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_unauth_get_album():
    client = APIClient()
    response = client.get('/albums/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_auth_get_album(auth_client):
    response = auth_client().get('/albums/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_auth_post(auth_client):
    #Create New DATA
    user= User.objects.create(username='Gamed',email='gamed@gmail.com',password1='yarb_tnf3', password2='yarb_tnf3')
    artist=Artist.objects.create(stage_name='Gamed',user=user)
    album = Album.objects.create(artist=artist, album_name='Struggling',release_time="2022-9-12" ,cost=199.0, is_approved=True)
    album_serializer= AlbumSerializer(album).data
    #Getting response
    response = auth_client().post('/albums/',album_serializer)
    assert response.status_code == 201 

@pytest.mark.django_db
def test_auth_post_fail(auth_client):
    #Create New DATA Missing Artist
    data ={"id": 1,
        "creation_time": "2022-9-12",
        "album_name": "Struggling",
        "release_time": "2022-12-12",
        "cost": 199.0,
        "is_approved": True}
    #Getting response
    response = auth_client().post('/albums/',data)
    assert response.status_code == 403 #FORBIDDEN


@pytest.mark.django_db
def test_unauth_post():
    client = APIClient()
    user= User.objects.create_user(username='Gamed',email='gamed@gmail.com',password1='yarb_tnf3', password2='yarb_tnf3')
    artist=Artist.objects.create(id=1 ,stage_name='Gamed',user=user)
    album = Album.objects.create(artist=artist,artist_id =1  ,release_time="2022-9-12" ,cost=199.0 ,is_approved=True)
    album_serializer= AlbumSerializer(album)
    
    response = client.post('/albums/',album_serializer.data)
    assert response.status_code == 401 #Unauthenticated



