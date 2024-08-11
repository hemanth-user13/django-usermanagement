from django.urls import path
from .views import RegisterView, LoginView, SuperAdminLoginView, RestaurantListView, RestaurantDetailView, FoodItemListView, FoodItemDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('superadmin-login/', SuperAdminLoginView.as_view(), name='superadmin-login'),
    
    # Restaurant URLs
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant-detail'),

    # Food Item URLs
    path('food-items/', FoodItemListView.as_view(), name='fooditem-list'),
    path('food-items/<int:pk>/', FoodItemDetailView.as_view(), name='fooditem-detail'),
]
