from django.contrib import admin
from .models import CustomUser, Restaurant, FoodItem

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_active', 'is_admin')
    search_fields = ('email', 'username')

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'photo', 'photo_url')
    search_fields = ('name', 'address')
    list_filter = ('name',)
@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price', 'quantity', 'discount', 'photo_url')  # Added photo_url
    search_fields = ('name', 'restaurant__name', 'photo_url')  # Added photo_url
    list_filter = ('restaurant', 'price')
