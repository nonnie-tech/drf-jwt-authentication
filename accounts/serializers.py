# accounts/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model

# Dynamically gets your active custom user model
User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    # password is write_only so it is never exposed in the API response JSON
    password = serializers.CharField(
        write_only=True, 
        required=True, 
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'phone_number')

    def create(self, validated_data):
        # Crucial: Use create_user() so Django securely hashes the password automatically
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number', '')
        )
        return user