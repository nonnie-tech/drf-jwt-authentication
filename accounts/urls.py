# accounts/urls.py
from django.urls import path
from .views import RegisterView, LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # Handles Login (Returns Access & Refresh tokens)
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # Refreshes expired access tokens
    path('logout/', LogoutView.as_view(), name='logout'), # Handles Logout (Blacklists the refresh token)
]