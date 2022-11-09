import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_get_fail():
    client = APIClient()
    
    response = client.get('/users/1/')
    assert response.status_code == 401


@pytest.mark.django_db
def test_get_auth_user(auth_client):

    response = auth_client().get('/users/1/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_put_fail():
    client = APIClient()
    
    response = client.put('/users/1/')
    assert response.status_code == 401


@pytest.mark.django_db
def test_put_auth_user(auth_client):

    response = auth_client().put('/users/1/')
    assert response.status_code == 200

@pytest.mark.django_db
def test_patch_fail():
    client = APIClient()
    
    response = client.patch('/users/1/')
    assert response.status_code == 401


@pytest.mark.django_db
def test_patch_auth_user(auth_client):

    response = auth_client().get('/users/1/')
    assert response.status_code == 200

