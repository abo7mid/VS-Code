from django.urls import path,include
from . import views


urlpatterns = [

    path('',views.index,),
    path('books',views.add_book),
    path('books/<int:id>',views.view_book),

    path('authors',views.authors),
    path('add_author',views.add_author),
    path('authors/<int:id>',views.view_author),
    
    path('addAuthorToBook',views.addAuthorToBook),
    path('addBookToAuthor',views.addBookToAuthor),


]