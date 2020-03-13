from django.urls import path
from .views import vessel

urlpatterns = [
    path('', vessel, name='vessel')
]