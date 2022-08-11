from re import template
from django.contrib import admin
from django.urls import path, include
from .views import *
from django.views.generic.base import TemplateView
from django.conf.urls.static import static

app_name= 'classifier'

urlpatterns = [
    path('xray', image_view, name = 'image_upload'),
    path('solver/<str:name>', solver, name = 'solver'),
    path('symptoms', view=symptoms, name='symptoms')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
