from rest_framework import serializers
from .models import UserRegistration

class RegisterMobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['phone', 'otp']