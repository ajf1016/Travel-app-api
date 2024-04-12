from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=200)
    featured_image = models.ImageField(upload_to='places/images/')
    place = models.CharField(max_length=200)
    category = models.ForeignKey("places.category", on_delete=models.CASCADE)
    description = models.TextField()
    is_deleted = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'places_places'
        verbose_name_plural = 'places'
    
    def __str__(self):
        return self.name
    

class Category(models.Model):
    image = models.ImageField(upload_to='category/images/')
    name = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'places_category'
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name
    

class Gallery(models.Model):
    image = models.ImageField(upload_to='places/images/')
    place = models.ForeignKey("places.place", on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'places_gallery'
        verbose_name_plural = 'gallery'
    
    def __str__(self):
        return str(self.id)