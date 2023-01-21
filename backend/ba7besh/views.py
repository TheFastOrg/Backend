# # your_app/views.py
# from rest_framework import generics
# from django.contrib.auth.models import User
# from .models import Restaurant, Review, BusinessInfo, Business, ReviewLike
# from .serializers import RestaurantSerializer, ReviewSerializer, BusinessInfoSerializer, BusinessSerializer, ReviewLikeSerializer

# class RestaurantCreateAPI(generics.CreateAPIView):
#     queryset = Restaurant.objects.all()
#     serializer_class = RestaurantSerializer

# class RestaurantDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Restaurant.objects.all()
#     serializer_class = RestaurantSerializer

# class ReviewCreateAPI(generics.CreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

# class ReviewDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

# class BusinessInfoCreateAPI(generics.CreateAPIView):
#     queryset = BusinessInfo.objects.all()
#     serializer_class = BusinessInfoSerializer

# class BusinessInfoDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = BusinessInfo.objects.all()
#     serializer_class = BusinessInfoSerializer

# class BusinessCreateAPI(generics.CreateAPIView):
#     queryset = Business.objects.all()
#     serializer_class = BusinessSerializer

# class BusinessDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Business.objects.all()
#     serializer_class = BusinessSerializer

# class ReviewLikeCreateAPI(generics.CreateAPIView):
#     queryset = ReviewLike.objects.all()
#     serializer_class = ReviewLikeSerializer

# class ReviewLikeDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = ReviewLike.objects.all()
#     serializer_class = ReviewLikeSerializer


from rest_framework import viewsets
from .models import Restaurant, Review, BusinessInfo, Business, ReviewLike
from .serializers import RestaurantSerializer, ReviewSerializer, BusinessInfoSerializer, BusinessSerializer, ReviewLikeSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class BusinessInfoViewSet(viewsets.ModelViewSet):
    queryset = BusinessInfo.objects.all()
    serializer_class = BusinessInfoSerializer

class BusinessViewSet(viewsets.ModelViewSet):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class ReviewLikeViewSet(viewsets.ModelViewSet):
    queryset = ReviewLike.objects.all()
    serializer_class = ReviewLikeSerializer
