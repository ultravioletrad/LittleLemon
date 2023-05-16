from django.contrib import admin 
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path,include 
from . import views  
from .views import BookingViewSet, MenuViewSet



router = routers.DefaultRouter()
router.register(r'menu-items', MenuViewSet)

urlpatterns = [
    
    path('menu-items/', MenuViewSet.as_view({'get': 'list'}), name='menu-items'),
    path('menu-items/<int:pk>/', MenuViewSet.as_view({'get': 'retrieve'}), name='single-menu-item'),
    path('message/', views.msg, name='message'),
    path('api-token-auth/', obtain_auth_token),
    path('', include(router.urls)),


]