from django.urls import path
from . import views
from . views import (Mobile_Phone_Register)
urlpatterns = [
    path('user-register/', Mobile_Phone_Register.as_view(), name='userregister'),
]