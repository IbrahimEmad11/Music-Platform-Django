from users.models import User
from artists.models import Artist
from ..models import Album
from ..serializers import AlbumSerializer
import pytest


@pytest.mark.django_db
def test_serializing_model():

    user= User.objects.create_user(username='Gamed',email='gamed@gmail.com',password1='yarb_tnf3', password2='yarb_tnf3')
    artist=Artist.objects.create(stage_name='Gamed',user=user)
    album = Album.objects.create(artist=artist, album_name='Struggling',release_time="2022-9-12" ,cost=199.0, is_approved=True)
    data= AlbumSerializer(album).data
    assert data['cost']== album.cost
    assert data['album_name']==album.album_name

@pytest.mark.django_db
def test_deserializing_model():

    user= User.objects.create_user(username='Gamed',email='gamed@gmail.com',password1='yarb_tnf3', password2='yarb_tnf3')
    artist=Artist.objects.create(stage_name='Gamed',user=user)
    album = Album.objects.create(artist=artist, album_name='Struggling',release_time="2022-9-12" ,cost=199.0, is_approved=True)
    data= AlbumSerializer(album).data
    expected_data = {'id': 1, 'creation_time': '2022-11-12', 'album_name': 'Struggling', 'release_time': '2022-9-12', 'cost': 199.0, 'is_approved': True, 'artist': 1}
    assert data['cost']== expected_data['cost']
    assert data['album_name']==expected_data["album_name"]