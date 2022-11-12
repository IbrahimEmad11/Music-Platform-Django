from .forms import AlbumForm,SongForm
from .models import Album,AlbumManager
from .serializers import AlbumSerializer
from .filters import AlbumFilter
from django.views.generic.edit import FormView,CreateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from django.urls import reverse_lazy
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters
from rest_framework.decorators import permission_classes




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


# class CustomAPIView(APIView):
#     def get_permissions(self):
#         # Instances and returns the dict of permissions that the view requires.
#         return {key: [permission() for permission in permissions] for key, permissions in self.permission_classes.items()}

#     def check_permissions(self, request):
#         # Gets the request method and the permissions dict, and checks the permissions defined in the key matching
#         # the method.
#         method = request.method.lower()
#         for permission in self.get_permissions()[method]:
#             if not permission.has_permission(request, self):
#                 self.permission_denied(
#                     request, message=getattr(permission, 'message', None)
#                 )

class AlbumList(ListAPIView):

    queryset=Album.approved_objects.all()
    serializer_class = AlbumSerializer
    permission_classes =  [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class =AlbumFilter

    # @permission_classes([permissions.AllowAny])
    def get(self ,*args, **kwargs):
        album=Album.approved_objects.all()
        serializers=AlbumSerializer(album,many=True)
        return Response(serializers.data , status=status.HTTP_200_OK)
   
    def post(self ,request):
        if 'artist' not in request.data.keys():
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializers=AlbumSerializer(data=request.data)
        if serializers.is_valid() :
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class AlbumListManual(ListAPIView):
    permission_classes = []
    serializer_class = AlbumSerializer
    def get_queryset(self):
        query = Album.approved_objects.all()
        try :
            query = query.filter(name__iexact = self.request.GET['name'])
        except:
            pass
        try:
            cost = int(self.request.GET['cost__gte'])
            query = query.filter(cost__gte = cost)
        except KeyError:
            pass
        except:
            raise TypeError("Cost must be integer")
        try :
            cost = int(self.request.GET['cost__lte'])
            query = query.filter(cost__lte = cost)
        except KeyError:
            pass
        except:
            raise TypeError("Cost must be integer")
        return query