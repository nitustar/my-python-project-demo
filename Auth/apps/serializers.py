from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields=['username', 'password', 'password2', 'email', 'role']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Both password is not same.")
        return data
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create_user(**validated_data)
        return user
    
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField(write_only=True)

    # class Meta:
    #     model=User
    #     fields=['id', 'username', 'email', 'role']

    def validate(self, validated_data):
        user=authenticate(username=validated_data['username'], password=validated_data['password'])
        if not user:
            raise serializers.ValidationError("User does not exist.")
        return user
        