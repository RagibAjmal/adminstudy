from io import BytesIO
from PIL import Image   

from django.core.files import File
from django.db import models

# Create your models here.
class Organizer(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField()

    class Meta:
        ordering=('name',)

    def __str__(self) :
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Events(models.Model):
    organizer=models.ForeignKey(Organizer,related_name="products",on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    slug=models.SlugField()
    mini_description=models.TextField(blank=True,null=True)
    detailed_description=models.TextField(blank=True,null=True)
    from_date=models.DateTimeField()
    to_date=models.DateTimeField()
    image=models.ImageField(upload_to='uploads/',blank=True,null=True)
    date_added=models.DateTimeField(auto_now_add=True)
    level=[
        "Beginner",
        "Intermediate",
        "Advanced"
    ]

        
    class Meta:
        ordering=('-date_added',)

    def __str__(self) :
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://admin.ragibajmal.study'+self.image.url   
        return ""
