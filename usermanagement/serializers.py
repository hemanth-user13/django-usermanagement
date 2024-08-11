from rest_framework import serializers
from .models import CustomUser, Restaurant, FoodItem

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'photo', 'photo_url']
        extra_kwargs = {
            'photo': {'required': False},
            'photo_url': {'required': False}
        }

    def validate(self, data):
        """
        Check that either 'photo' or 'photo_url' is provided, not both.
        """
        if data.get('photo') and data.get('photo_url'):
            raise serializers.ValidationError("Provide either a photo file or a photo URL, not both.")
        return data

class FoodItemSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    
    class Meta:
        model = FoodItem
        fields = ['id', 'restaurant', 'name', 'description', 'price', 'quantity', 'discount', 'photo_url']
