from django.shortcuts import render

# Create your views here.
# accounts/views.py
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from .serializers import RegisterSerializer

User = get_user_model()

# 1. Registration View (Anyone can access)
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

# 2. Logout View (Requires authentication to blacklist the refresh token)
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            # Expects the client to send the refresh token in the body
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            
            # Blacklist the token so it can never be used to get a new access token again
            token.blacklist()
            
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid token or token missing."}, status=status.HTTP_400_BAD_REQUEST)