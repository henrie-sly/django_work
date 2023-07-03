from django.urls import path
from .views import collect, arrange

urlpatterns = [
    path('list/', collect, name = 'list'),
    path('order/', arrange, name = 'order')
]