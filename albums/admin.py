import imp
from django.contrib import admin
from .models import Album
from django import forms

# Register your models here.
class AlbumForm(forms.ModelForm):

  class Meta:
    model = Album
    exclude =()
    help_texts = {'approve':"Approve the album if its name is not explicit",}



class AlbumAdmin(admin.ModelAdmin):

    readonly_fields = ('creation_time',)
    form=AlbumForm
    actions = ['approve_list']
    @admin.action(description='Select Approved Albums')

    def approve_list(self, request, queryset):
      queryset.update(is_approved=True)

    

admin.site.register(Album,AlbumAdmin)