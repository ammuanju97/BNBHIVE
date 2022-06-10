from rest_framework import serializers
from .models import UserRegistration
from random import randint
from rest_framework.validators import UniqueValidator

class OtpSerializer(serializers.ModelSerializer):
    def validate_phone_number(self, phone):
        if phone_regex:
            phone= re.compile('^(?:\+?88)?01[13-9]\d{8}$')
            if phone_regex.match(phone):
                return (phone)
            else:
                raise serializers.ValidationError('No. not matching')
        else:
            raise serializers.ValidationError('Please enter a number')

    def generate_otp(self):
        otp = randint(000000, 999999)
        return otp
    class Meta:
        model = UserRegistration
        fields = ['phone', 'otp']


class VerifyOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ['phone']


class UserSerializer(serializers.ModelSerializer):
   
    first_name = serializers.CharField(min_length=8)
    last_name = serializers.CharField(min_length=8)
    date_of_birth = serializers.DateField()
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=UserRegistration.objects.all())]
            )
    def create(self, validated_data):
        user = UserRegistration.objects.create_user(validated_data['first_name'],
            validated_data['last_name'],
             validated_data['date_of_birth'], validated_data['email'])
        return user

    class Meta:
        model = UserRegistration
        fields = ('first_name','last_name', 'date_of_birth', 'email')