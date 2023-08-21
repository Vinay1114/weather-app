from django.urls import path,include
from .views import get_weather

urlpatterns = [
    path('get-weather/', get_weather, name='get-weather'),
    
]
