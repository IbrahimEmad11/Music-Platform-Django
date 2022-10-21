from django.contrib import admin
from albums.models import Album
from .models import Artist

# Register your models here.


class ArtistAdmin(admin.ModelAdmin):
    
    list_display=['stage_name','social_link','approved_albums']

    def approved_albums(self, obj):
        return obj.album_set.filter(is_approved=True).count()

admin.site.register(Artist,ArtistAdmin)