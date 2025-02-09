from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('foods/', views.food_list, name='food_list'),  # List all foods
    path('foods/<int:pk>/', views.food_detail, name='food_detail'),  # Food detail
    path('foods/create/', views.food_create, name='food_create'),  # Create food
    path('foods/<int:pk>/update/', views.food_update, name='food_update'),  # Update food
    path('foods/<int:pk>/delete/', views.food_delete, name='food_delete'),  # Delete food
     path('signup/', views.signup, name='signup'), 
]