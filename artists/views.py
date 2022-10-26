from .models import Artist
from albums.models import Album
from django.views.generic import ListView, FormView
from .forms import ArtistForm

from artists.models import Artist
from artists.serializers import ArtistSerializer
from rest_framework import generics


class ArtistView(FormView):
    template_name = 'create_artist.html'
    form_class = ArtistForm
    success_url = "."

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ArtistList(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

