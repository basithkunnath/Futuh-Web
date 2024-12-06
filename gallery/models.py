from django.db import models

# Create your models here.


class Gallery(models.Model):
    gallery_image = models.ImageField(upload_to='gallery_images/', blank=True, null=True)
    
def __str__(self):
        return str(self.pk)