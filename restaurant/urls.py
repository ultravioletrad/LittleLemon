from django.contrib import admin 
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path,include 
from . import views  
from .views import BookingViewSet, MenuViewSet



router = routers.DefaultRouter()
router.register(r'menu-items', MenuViewSet, basename='menu-items')


urlpatterns = [

    path('message/', views.msg, name='message'),
    path('api-token-auth/', obtain_auth_token),
    path('', include(router.urls)),

]