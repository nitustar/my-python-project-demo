from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, LoginSerializer    

# Create your views here.
@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    return Response({'status': 'OK', "message": "Healthy"})

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response(
            {
                'message': 'User Created!',
                'user':{
                    'id':user.id,
                    'username':user.username,
                    'email':user.email,
                    'role':user.role
                }
            }, status=201
        )

class LoginView(APIView):
    permission_classes=[AllowAny]

    def post(self, request):
        serializer=LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data.get('user')
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                'user': {
                    'id':user.id,
                    'username':user.username,
                    'role':user.role
                },
                'access': str(refresh.access_token),
                'refresh': str(refresh)
            }, status=205
        )

# class LogoutView(APIView):
#     permission_classes=[IsAuthenticated]

#     def post(self, request):