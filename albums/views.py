from cgitb import html
from xmlrpc.client import DateTime
from django.shortcuts import render
from pyexpat import model
from .models import Artist
from albums.models import Album
from django import forms



class AlbumForm(forms.ModelForm):

    release_time= forms.DateField(widget=forms.DateInput)
    class Meta:
     model = Album
     fields = '__all__'
     

def create_album(request):

    if request.method=='POST':
        form=AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            form = AlbumForm()
        
        
    
    else:
        form =AlbumForm()
    return render(request,'create_album.html', {'form': form})