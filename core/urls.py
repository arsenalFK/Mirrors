from django.urls import path
from . import views
from .views import Base, Mirrors, Home

urlpatterns = [
    path('', Base.as_view(), name='base'),
    path('products/', Mirrors.as_view(), name='main'),
]