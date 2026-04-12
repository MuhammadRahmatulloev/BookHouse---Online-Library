from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    
    path('categories/', views.category_list_view, name='category_list'),
    path('categories/<int:pk>/', views.category_detail_view, name='category_detail'),
    path('categories/create/', views.category_create_view, name='category_create'),
    path('categories/<int:pk>/update/', views.category_update_view, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete_view, name='category_delete'),

    path('authors/', views.author_list_view, name='author_list'),
    path('authors/<int:pk>/', views.author_detail_view, name='author_detail'),
    path('authors/create/', views.author_create_view, name='author_create'),
    path('authors/<int:pk>/update/', views.author_update_view, name='author_update'),
    path('authors/<int:pk>/delete/', views.author_delete_view, name='author_delete'),

    path('publishers/', views.publisher_list_view, name='publisher_list'),
    path('publishers/<int:pk>/', views.publisher_detail_view, name='publisher_detail'),
    path('publishers/create/', views.publisher_create_view, name='publisher_create'),
    path('publishers/<int:pk>/update/', views.publisher_update_view, name='publisher_update'),
    path('publishers/<int:pk>/delete/', views.publisher_delete_view, name='publisher_delete'),

    path('books/', views.book_list_view, name='book_list'),
    path('books/<int:pk>/', views.book_detail_view, name='book_detail'),
    path('books/create/', views.book_create_view, name='book_create'),
    path('books/<int:pk>/update/', views.book_update_view, name='book_update'),
    path('books/<int:pk>/delete/', views.book_delete_view, name='book_delete')
]