from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name= 'index'),
    path('add_book', views.add_book, name='add_book'),
    path('books/<int:id>/',views.books,name='books'),
    path('books/<int:book_id>/add_author/', views.add_author_to_book_view, name='add_author_to_book'),

    path('add_author/', views.add_author_view, name='add_author'),
    path('authors/<int:id>', views.authors, name='authorinfo'),
    path('authors/<int:author_id>/add_book/', views.add_book_to_author_view, name='add_book_to_author'),
        

    


    
    
]