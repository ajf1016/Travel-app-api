from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.v1.places.serializers import PlaceSerializer
from places.models import Place

@api_view(['GET'])
def places(request):
    instance = Place.objects.filter(is_deleted=False)
    context = {
        "request" : request
    }
    serializer = PlaceSerializer(instance,many=True,context=context)
    
    response_data = {
        "status_code" : 6000,
        "data" : serializer.data
    }
    return Response(response_data)