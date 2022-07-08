from django.urls import path
from  . import views
urlpatterns = [
	path('', views.index, name='index'),
	path('books', views.books, name='books'),
	path('books/<int:bookId>', views.viewBook, name='viewBook'),
	path('favorite/<int:bookId>', views.addToFavorite, name='Favorite'),
	path('editBook/<int:bookId>', views.bookEdit, name='editBook'),
	path('logout', views.logout, name='logout'),
]


#
