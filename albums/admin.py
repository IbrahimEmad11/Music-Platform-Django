from django.contrib import admin
from .models import Album,Song
from django import forms
from .forms import AlbumForm,Forcing

# Register your models here.
class SongInline(admin.TabularInline):
    model = Song
    formset = Forcing
    extra =1


class AlbumAdmin(admin.ModelAdmin):

    readonly_fields = ('creation_time',)
    form=AlbumForm
    actions = ['approve_list']
    inlines = [SongInline,]
    @admin.action(description='Select Approved Albums')

    def approve_list(self, request, queryset):
      queryset.update(is_approved=True)


admin.site.register(Album,AlbumAdmin)   
admin.site.register(Song)



