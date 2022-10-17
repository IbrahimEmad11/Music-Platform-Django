from django.shortcuts import render
from pyexpat import model
from django.views.generic import ListView
from django.core.exceptions import ValidationError
from .models import Artist
from albums.models import Album
from django import forms



class ArtistForm(forms.ModelForm):
   class Meta:
     model = Artist
     fields = '__all__'

def create_artist(request):

    if request.method=='POST':
        form=ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            form = ArtistForm()
        
    
    else:
        form =ArtistForm()
    return render(request,'create_artist.html', {'form': form})

class ArtistList(ListView):

    model = Artist
    template_name='artist_list.html'
    context_object_name = 'artists'

    def get_context_data(self, **kwargs):
        
        
        context = super(ArtistList, self).get_context_data(**kwargs)
        context['approved'] = Album.objects.all()
        return context

