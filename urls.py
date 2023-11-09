from django.urls import path
from . import views
urlpatterns = [
    path('',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('team/',views.group,name='team'),
    path('booking/',views.booking,name='booking'),
    path('logout/',views.logout,name='logout'),
     path('register/',views.register,name='register'),
]