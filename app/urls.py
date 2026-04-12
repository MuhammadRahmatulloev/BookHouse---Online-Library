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
    path('author/<int:pk>/delete/', views.author_delete_view, name='author_delete'),

    path('publisher/', views.publisher_list_view, name='publisher_list'),
    path('publisher/<int:pk>/', views.publisher_detail_view, name='publisher_detail'),
    path('publisher/create/', views.publisher_create_view, name='publisher_create'),
    path('publisher/<int:pk>/update/', views.publisher_update_view, name='publisher_update'),
    path('publisher/<int:pk>/delete/', views.publisher_delete_view, name='publisher_delete'),

    path('book/', views.book_list_view, name='book_list'),
    path('book/<int:pk>/', views.book_detail_view, name='book_detail'),
    path('book/create/', views.book_create_view, name='book_create'),
    path('book/<int:pk>/update/', views.book_update_view, name='book_update'),
    path('book/<int:pk>/delete', views.book_delete_view, name='book_delete')
]