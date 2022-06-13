from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    # views.login is a function gets invoked whenever someones go to the route '/login'
    path('login', views.login),
    # use <str:name> whenever you want to pass a string in the route '/' ex /John
    # path('<str:name>',views.index), 

    path('another_route',views.another_method),
    path('redirected_route',views.redirected_method)
    
]
