import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_register():
    client = APIClient()
    info_dict = dict(username = "IbrahimE11" ,password= "lmao1234")
    response = client.post('/authentication/register/',info_dict)
    data =response.data
    print(data)
    assert 'password' not in data


@pytest.mark.django_db
def test_login_fail():
    client = APIClient()
    info_dict = dict(username = "awq",password = "is",)
    response = client.post('/authentication/login/',info_dict)
    assert response.status_code == 400


@pytest.mark.django_db
def test_auth_login_fail(auth_client):

    info_dict = dict(username = "gamed")
    response = auth_client().post('/authentication/login/',info_dict)
    assert response.status_code == 400

@pytest.mark.django_db
def test_auth_login(auth_client):

    info_dict = dict(username = "IbrahimE11" ,password= "lmao1234")
    response = auth_client().post('/authentication/login/',info_dict)
    assert response.status_code == 200
