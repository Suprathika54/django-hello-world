from django.urls import path
from . import views

urlpatterns = [
    #path('', hello_world_json, name='hello_world_json'),
    path('', views.hello_world_html, name='hello_world_html'),
]

