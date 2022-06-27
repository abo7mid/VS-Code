from django.urls import path,include
from . import views


urlpatterns = [
path('',views.index),
path('success',views.success),
path('logout',views.logout),
]
