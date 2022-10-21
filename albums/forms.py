from django import forms
from .models import Album
from django.forms.models import BaseInlineFormSet

class Forcing(BaseInlineFormSet):

    def clean(self):
       
        super(Forcing, self).clean()
        if any(self.errors):
            return
        if not any(cleaned_data and not cleaned_data.get('DELETE', False)
            for cleaned_data in self.cleaned_data):
            raise forms.ValidationError('At least one item required.')

class AlbumForm(forms.ModelForm):

    release_time= forms.DateField(widget=forms.DateInput)
    class Meta:
     model = Album
     fields = '__all__'
     help_texts = {'approve':"Approve the album if its name is not explicit",}

from .models import Song

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ('album', 'name', 'img')

    def clean(self):
        cleaned_data = super().clean()
        field_name = cleaned_data.get('name')

        if len(field_name) <= 0 or field_name == '':
            aaa = cleaned_data['album'].album_name
            cleaned_data['name'] = aaa
            print('cleaned_data', cleaned_data)