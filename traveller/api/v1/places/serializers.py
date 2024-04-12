from rest_framework.serializers import ModelSerializer
from places.models import Place
from rest_framework import serializers


class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = ("id","name","featured_image","place")
        
        
class PlaceDetailSerializer(ModelSerializer):
    category = serializers.SerializerMethodField()
    class Meta:
        model = Place
        fields = "__all__"
    
    def get_category(self,instance):
        return instance.category.name