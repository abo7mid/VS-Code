from django.urls import path
from . import views

urlpatterns = [
    # CRUD = Create, Read, Update, Delete

    # Root page redirect to main page
    path('', views.index),
    # main page implement Read all
    path('shows', views.shows, name="shows"),

    # when click add new show, html redirect to Create
    path('shows/new', views.addShow, name="add"),

    # when click create implement Create
    path('shows/create', views.createShow, name="create"),

    # when click show implement Read
    path('shows/<int:id>/view', views.viewShow, name="view"),

    # when click delete implement Delete
    path('shows/<int:id>/delete', views.deleteShow, name="delete"),

    # when click edit implement update method
    path('shows/<int:id>/edit', views.editShow, name="edit"),

    # when click update implement update method
    # path('shows/<int:id>/update',views.updateShow,name="update"),

]

# potential errors
# OperationalError no such table: TV_Shows_show
# NoReverseMatch   Reverse for 'update' not found. 'update' is not a valid view function or pattern name
# ValueError       too many values to unpack (expected 2) the cause "I forget to append () to the end fo the function"
# AttributeError   'str' object has no attribute 'get'