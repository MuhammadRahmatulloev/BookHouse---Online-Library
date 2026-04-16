from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('stats/', stats_view, name='stats'),
    
    path('categories/', category_list_view, name='category_list'),
    path('categories/<int:pk>/', category_detail_view, name='category_detail'),
    path('categories/create/', category_create_view, name='category_create'),
    path('categories/<int:pk>/update/', category_update_view, name='category_update'),
    path('categories/<int:pk>/delete/', category_delete_view, name='category_delete'),

    path('authors/', author_list_view, name='author_list'),
    path('authors/<int:pk>/', author_detail_view, name='author_detail'),
    path('authors/create/', author_create_view, name='author_create'),
    path('authors/<int:pk>/update/', author_update_view, name='author_update'),
    path('authors/<int:pk>/delete/', author_delete_view, name='author_delete'),

    path('publishers/', publisher_list_view, name='publisher_list'),
    path('publishers/<int:pk>/', publisher_detail_view, name='publisher_detail'),
    path('publishers/create/', publisher_create_view, name='publisher_create'),
    path('publishers/<int:pk>/update/', publisher_update_view, name='publisher_update'),
    path('publishers/<int:pk>/delete/', publisher_delete_view, name='publisher_delete'),

    path('books/', book_list_view, name='book_list'),
    path('books/<int:pk>/', book_detail_view, name='book_detail'),
    path('books/create/', book_create_view, name='book_create'),
    path('books/<int:pk>/update/', book_update_view, name='book_update'),
    path('books/<int:pk>/delete/', book_delete_view, name='book_delete'),

    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('change/', change_password_view, name='change'),
    path('forgot/', forgot_password_view, name='forgot'),
    path('logout/', logout_view, name='logout')
]