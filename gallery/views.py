from django.shortcuts import render
from .models import Gallery_Page
# Create your views here.


def gallery(request):
    view_gallery = Gallery_Page.objects.all()
    context = {
        'list_gallery_img': view_gallery
    }
    return render(request, 'gallery.html',context)
