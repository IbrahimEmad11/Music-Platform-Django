from django.urls import path
from .views import UserAPI




urlpatterns=[
    path('<pk>/', UserAPI.as_view(), name='user_api'),
]