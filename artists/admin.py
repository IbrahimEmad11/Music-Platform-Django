from django.contrib import admin
from albums.models import Album
from .models import Artist

# Register your models here.
class AlbumInline(admin.TabularInline):
    model = Album
    extra=1

class ArtistAdmin(admin.ModelAdmin):
    inlines = [AlbumInline,]
    list_display=['stage_name','social_link','approved_albums']

    def approved_albums(self, obj):
        return obj.album_set.filter(is_approved=True).count()

admin.site.register(Artist,ArtistAdmin)