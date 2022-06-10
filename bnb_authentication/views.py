from .models import UserRegistration
from .serializers import VerifyOTPSerializer, OtpSerializer, UserSerializer
from rest_framework import permissions
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import  AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from random import randint


class GetOTP(CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = UserRegistration.objects.all()
    serializer_class = OtpSerializer

    def perform_create(self, serializer):
        serializer.save(otp=randint(000000, 999999))


class VerifyOTP(APIView):
    
    permission_classes = (permissions.AllowAny, )
    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone' , False)
        otp_sent = request.data.get('otp', False)
        if phone and otp_sent:
            old = UserRegistration.objects.filter(phone__iexact = phone)
            if old.exists():
                old = old.first()
                otp = old.otp
                if str(otp_sent) == str(otp):
                    old.validated = True
                    old.save()
                    return Response({
                        'status' : True,
                        'detail' : 'OTP mactched. Please proceed for registration.'
                        })
                else: 
                    return Response({
                        'status' : False,
                        'detail' : 'OTP incorrect.'
                        })
            else:
                return Response({
                    'status' : False,
                    'detail' : 'First proceed via sending otp request.'
                    })
        else:
            return Response({
                'status' : False,
                'detail' : 'Please provide both phone and otp for validations'
                })


class UserRegister(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
