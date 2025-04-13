import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST, require_GET
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.utils import timezone

# Create your views here.

def home(request):
    return JsonResponse({"message":"Welcome to the Job Portal App", "status":200})

@require_POST
@csrf_exempt
def create_user(request):
    data = request.body
    py_dict = json.loads(data)
    username = py_dict.get('username')
    email = py_dict.get('email')
    password = py_dict.get('password')
    user = User.objects.create_user(username=username, email=email, password=password)
    json_response = serializers.serialize('json', [user])
    return JsonResponse({'message': 'User created successfully'})

@require_GET
def all_users(request):
    users = User.objects.get(pk=1)
    json_users = serializers.serialize('json', [users])
    return JsonResponse({"message": json_users})
    # return HttpResponse(users)