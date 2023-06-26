# your_app/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from enumfields import EnumField
from .models import Restaurant, Review, BusinessInfo, Business, ReviewLike
from enum import Enum


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'address')

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    class Meta:
        model = Review
        fields = ('id', 'user', 'restaurant', 'review_text')

class BusinessInfoSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    class Meta:
        model = BusinessInfo
        fields = ('id', 'restaurant', 'phone_number', 'location')

class BusinessSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())
    class Meta:
        model = Business
        fields = ('id', 'user', 'restaurant')

class ReviewLikeSerializer(serializers.ModelSerializer):
    review = serializers.PrimaryKeyRelatedField(queryset=Review.objects.all())
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    class Meta:
        model = ReviewLike
        fields = ('id', 'review', 'user')
