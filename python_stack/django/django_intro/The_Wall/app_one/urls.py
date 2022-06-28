from django.urls import path
from  . import views




urlpatterns = [
path('',views.index),
path('wall',views.wall),
path('logout',views.logout),
]
