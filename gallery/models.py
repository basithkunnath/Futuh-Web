from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.


class Gallery(models.Model):
 gallery_image = CloudinaryField('image', default='path/to/default-image.jpg')
    
def __str__(self):
        return str(self.pk)