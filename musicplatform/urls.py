from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('artists/', include('artists.urls')),
    path('albums/', include('albums.urls')),
    path('login/', include('users.urls')),
    path('login/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)