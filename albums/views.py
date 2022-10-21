from .forms import AlbumForm,SongForm
from django.views.generic.edit import FormView,CreateView
from django.urls import reverse_lazy

class AlbumView(FormView):
    template_name = 'create_album.html'
    form_class = AlbumForm
    success_url = "."

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class SongView(CreateView):
    template_name = 'create_song.html'
    form_class = SongForm
    success_url = reverse_lazy('song')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context