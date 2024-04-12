from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.v1.places.serializers import PlaceSerializer,PlaceDetailSerializer
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


@api_view(['GET'])
def place(request,pk):
    if  Place.objects.filter(pk=pk).exists():
        instance = Place.objects.get(pk=pk)
        context = {
            "request" : request
        }
        serializer = PlaceDetailSerializer(instance,context=context)
        
        response_data = {
            "status_code" : 6000,
            "data" : serializer.data
        }
        return Response(response_data)
    else:
        response_data = {
            "status_code" : 6001,
            "message" : "Place not found"
        }
        return Response(response_data)