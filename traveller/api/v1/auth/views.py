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

        response_data = {
            "status_code": 6000,
            "message": "User cretaed successfully",
        }
        return Response(response_data)
    else:
        response_data = {
            "status_code": 6001,
            "message": "User with email '%s' already exists" % email,
        }
        return Response(response_data)
