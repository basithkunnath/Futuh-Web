from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('gallery/', views.gallery, name='gallery'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)