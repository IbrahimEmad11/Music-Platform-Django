import pytest
from rest_framework.test import APIClient
from users.models import User
from django.contrib.auth import authenticate

@pytest.fixture()
def auth_client(db):
    def get_user(auth_user=None):

        client = APIClient()

        if auth_user is None :
            user= User.objects.create_user(username='IbrahimE11', password= "lmao1234")
            user.save()
            auth_user= authenticate(username='IbrahimE11', password= "lmao1234")

            info_dict = dict(
                username = "IbrahimE11",
                password = "lmao1234",
            )
            response= client.post ('/authentication/login/' , info_dict ,format='json')
            data=response.data
            token=data['token']
            
            client.credentials (HTTP_AUTHORAIZATION = 'Token'+ token)
            client.force_authenticate(user=auth_user)

        else:
            client.force_authenticate(user=auth_user)
        return client
    return get_user