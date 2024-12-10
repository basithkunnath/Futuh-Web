from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Gallery_Page(models.Model):
    gallery_img = CloudinaryField('image')
    
def __str__(self):
        return str(self.pk)