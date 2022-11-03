from users.models import User
from rest_framework.response import Response
from authentication.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class UserAPI(APIView):
  
    permission_classes = [IsAuthenticated]

    def get(self,request,pk,*args,**kwargs):
        try:
            user = User.objects.get(pk=pk)
            return Response(UserSerializer(user).data,status= 200)
        except User.DoesNotExist:
            return Response(status=404,data="No User Found")
    
    def put(self,request,pk):
     
        try :
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response("Updated Successfully!")
            else :
                return Response("Invalid Data!")
        except :
            return Response("No User Found")
    
    def patch(self,request,pk):
       
        try :
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user,data = request.data , partial = True)
            if serializer.is_valid():
                serializer.save()
                return Response("Updated Successfully!")
            else :
                return Response("Invalid Data!")
        except :
             return Response("No User Found")
