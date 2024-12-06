from django.db import models

# Create your models here.


class AboutPage(models.Model):
    about_page_title = models.CharField(max_length=100)
    about_page_first_paragraph = models.TextField(null=True)
    about_page_second_paragraph = models.TextField(null=True)
    about_page_image_1 = models.ImageField(upload_to='about_page_images/', blank=True, null=True)
    our_values_title = models.CharField(max_length=100)
    our_values_sub_title_1 = models.CharField(max_length=100)
    our_values_content_1 = models.TextField()
    our_values_sub_title_2 = models.CharField(max_length=100)
    our_values_content_2 = models.TextField()
    our_values_sub_title_3 = models.CharField(max_length=100)
    our_values_content_3 = models.TextField()
    why_choose_us_title = models.CharField(max_length=100)
    why_choose_us_first_paragraph = models.TextField()
    why_choose_us_second_paragraph = models.TextField()
    about_page_image_2 = models.ImageField(upload_to='about_page_images/', blank=True, null=True)



    def str(self):
        return "About Page Content"
    


class Testimonial(models.Model):
    client_image = models.ImageField(upload_to='client_images/', blank=True, null=True)
    client_name = models.CharField(max_length=100)
    client_words = models.TextField(null=True)
    

    def __str__(self):
        return self.client_name
