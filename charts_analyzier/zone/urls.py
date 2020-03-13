from django.urls import path
from .views import zone

urlpatterns = [
    path('', zone, name='zone')
]