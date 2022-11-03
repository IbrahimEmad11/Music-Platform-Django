from rest_framework import serializers
from users.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
        
    def validate(self, data):

        if len(data.get('password1')) < 8:
            raise serializers.ValidationError("Password must be 8 characters or more")

        if not data.get('password1') or not data.get('password2'):
            raise serializers.ValidationError("Please enter a password and "
                                              "confirm it.")
        if data.get('password1') != data.get('password2'):
            raise serializers.ValidationError("Those passwords don't match.")
        return data
        
       


# ------------------------------------------------ #

# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField()

#     def validate(self, data):
#         user = authenticate(**{'username': data['email'], 'password': data['password']})
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError('Incorrect Credentials Passed.')
