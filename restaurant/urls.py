from django.contrib import admin 
from rest_framework import routers
from django.urls import path 
from . import views  
from .views import BookingViewSet, MenuViewSet, UserViewSet



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'menu', MenuViewSet)
router.register(r'booking', BookingViewSet)

urlpatterns = [
    path('', views.home, name='home'),
] + router.urls


