from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.category_list_view, name='category_list'),
    path('categories/<int:pk>/', views.category_detail_view, name='category_detail'),
    path('categories/create/', views.category_create_view, name='category_create'),
    path('categories/<int:pk>/update/', views.category_update_view, name='category_update'),
    path('categories/<int:pk>/delete/', views.category_delete_view, name='category_delete'),
]