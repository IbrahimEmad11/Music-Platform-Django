from django_filters import rest_framework as filters
from .models import Album


class AlbumFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='album_name',lookup_expr='iexact')
    cost = filters.NumberFilter()
    cost__gt = filters.NumberFilter(field_name='cost', lookup_expr='gt')
    cost__lt = filters.NumberFilter(field_name='cost', lookup_expr='lt')

    class Meta:
        model = Album
        fields = ['cost', 'album_name']