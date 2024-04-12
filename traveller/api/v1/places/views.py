from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def places(request):
    return Response("Hello ...this is placess")