import requests
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def create_user(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    username = request.POST.get('username')

    if not User.objects.filter(email=email).exists():
        User.objects.create_user(
            email=email, password=password, username=username)

        headers = {
            'content-type': 'application/json',
        }

        protocol = 'http://'
        if request.is_secure():
            protocol = 'https://'
        host = request.get_host()
        login_url = protocol + host + '/api/v1/auth/token/'

        data = {
            "username": username,
            "password": password,
            "email": email,
        }

        response = requests.post(
            login_url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            response_data = {
                "status_code": 6000,
                "message": "User cretaed successfully",
                "data": response.json(),
            }
            return Response(response_data)
        else:
            response_data = {
                "status_code": 6001,
                "message": "An error occured while creating user. Please try again later.",
            }
            return Response(response_data)
    else:
        response_data = {
            "status_code": 6001,
            "message": "User with email '%s' already exists" % email,
        }
        return Response(response_data)
