from django.urls import path

from publishers import views

urlpatterns = [
    path('', views.publishers_list, name='publishers_list'),
    path('create/', views.create_publisher, name='create_publisher'),
    path('details/<int:pk>/', views.publisher_details, name='publisher_details'),
    path('edit/<int:pk>', views.edit_publisher, name='edit_publisher'),
    path('delete/<int:pk>', views.delete_publisher, name='delete_publisher'),
]