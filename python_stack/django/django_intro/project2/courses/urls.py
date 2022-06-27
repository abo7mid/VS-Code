from django.urls import path
from . import views

urlpatterns = [

    path('',views.index),
    path('courses/destroy/<int:id>',views.destroy,name="remove"),
]