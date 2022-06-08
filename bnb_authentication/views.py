from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import UserRegistration
from .serializers import RegisterMobileSerializer

# @csrf_exempt
def UserRegister(request):
    
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegisterMobileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)