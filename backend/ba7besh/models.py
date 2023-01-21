from django.db import models
from django.contrib.auth.models import User
from enumfields import EnumField
from enum import Enum

class LikeType(Enum):
    UPVOTE = 'upvote'
    DOWNVOTE = 'downvote'

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    review_text = models.TextField()

class BusinessInfo(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class ReviewLike(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = EnumField(LikeType, max_length=255)

    class Meta:
        unique_together = (("review", "user"),)