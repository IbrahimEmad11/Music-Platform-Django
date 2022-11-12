from .models import Artist
from artists.models import Artist
from artists.serializers import ArtistSerializer
from rest_framework import generics



class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

