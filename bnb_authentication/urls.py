from django.urls import path
from . import views
from . views import (VerifyOTP, GetOTP, UserRegister)
urlpatterns = [
    
    path('mobile-otp/', GetOTP.as_view(), name='mobileotp'),
    path('verify-otp/', VerifyOTP.as_view(), name='veriftotp'),
    path('user-register/', UserRegister.as_view(), name='userregister'),
]