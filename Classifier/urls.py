
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.views.generic.base import TemplateView
from django.conf.urls.static import static

app_name= 'classifier'

urlpatterns = [
    path('', TemplateView.as_view(template_name='Classifier\home.html') ),
    path('symptoms', view=symptoms, name='symptoms')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
