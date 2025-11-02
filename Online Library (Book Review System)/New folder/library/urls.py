from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/<int:pk>/review/', views.add_review, name='add_review'),
    path('review/<int:pk>/edit/', views.edit_review, name='edit_review'),
    path('review/<int:pk>/delete/', views.delete_review, name='delete_review'),
    path('category/<int:category_id>/', views.books_by_category, name='books_by_category'),
    
    # Admin URLs
    path('admin-panel/', views.admin_dashboard, name='admin_dashboard'),
    
    # User Management
    path('admin-panel/users/', views.admin_users, name='admin_users'),
    path('admin-panel/users/add/', views.admin_add_user, name='admin_add_user'),
    path('admin-panel/users/<int:user_id>/edit/', views.admin_edit_user, name='admin_edit_user'),
    path('admin-panel/users/<int:user_id>/delete/', views.admin_delete_user, name='admin_delete_user'),
    
    # Book Management
    path('admin-panel/books/', views.admin_books, name='admin_books'),
    path('admin-panel/books/add/', views.admin_add_book, name='admin_add_book'),
    path('admin-panel/books/<int:book_id>/edit/', views.admin_edit_book, name='admin_edit_book'),
    path('admin-panel/books/<int:book_id>/delete/', views.admin_delete_book, name='admin_delete_book'),
    
    # Category Management
    path('admin-panel/categories/', views.admin_categories, name='admin_categories'),
    path('admin-panel/categories/add/', views.admin_add_category, name='admin_add_category'),
    path('admin-panel/categories/<int:category_id>/edit/', views.admin_edit_category, name='admin_edit_category'),
    path('admin-panel/categories/<int:category_id>/delete/', views.admin_delete_category, name='admin_delete_category'),
]