from .models import Artist
from albums.models import Album
from django.views.generic import ListView, FormView
from .forms import ArtistForm


class ArtistView(FormView):
    template_name = 'create_artist.html'
    form_class = ArtistForm
    success_url = "."

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ArtistList(ListView):

    model = Artist
    template_name='artist_list.html'
    context_object_name = 'artists'

    def get_context_data(self, **kwargs):
        
        
        context = super(ArtistList, self).get_context_data(**kwargs)
        context['approved'] = Album.objects.all()
        return context

