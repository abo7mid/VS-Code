from django.urls import path,include
from . import views

app_name = 'surveys'

urlpatterns = [
    path('surveys',views.surveys),
    path('surveys/new',views.new_surveys),
]