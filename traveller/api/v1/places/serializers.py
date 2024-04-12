from rest_framework.serializers import ModelSerializer
from places.models import Place,Gallery
from rest_framework import serializers


class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = ("id","name","featured_image","place")
        
        
class GallerySerializer(ModelSerializer):
    class Meta:
        model = Gallery
        fields = ("id","image")
        
        
class PlaceDetailSerializer(ModelSerializer):
    category = serializers.SerializerMethodField()
    gallery = serializers.SerializerMethodField()
    
    class Meta:
        model = Place
        fields = "__all__"
    
    def get_category(self,instance):
        return instance.category.name
    
    def get_gallery(self,instance):
        context = {
            "request" : self.context.get('request')
        }
        images = Gallery.objects.filter(place=instance)
        serializers = GallerySerializer(images,many=True,context=context)
        return serializers.data