from django.urls import path

from categories import views

urlpatterns = [
    path('', views.categories_list, name='categories_list'),
    path('create/', views.create_category, name='create_category'),
    path('details/<int:pk>/', views.category_details, name='category_details'),
    path('edit/<int:pk>', views.edit_category, name='edit_category'),
    path('delete/<int:pk>', views.delete_category, name='delete_category'),
]