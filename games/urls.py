from django.urls import path

from games import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_game, name='create_game'),
    path('details/<int:pk>/', views.game_details, name='game_details'),
    path('edit/<int:pk>/', views.edit_game, name='edit_game'),
    path('delete/<int:pk>/', views.delete_game, name='delete_game'),
]