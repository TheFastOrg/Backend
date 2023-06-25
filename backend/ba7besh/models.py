import time

from django.contrib.gis.geos import Point
from django.db import models
from django.contrib.auth.models import User
from enumfields import EnumField
from enum import Enum


class BaseModel(models.Model):  # base class should subclass 'django.db.models.Model'

    created_at = models.DateTimeField(default=time.time())
    updated_at = models.DateTimeField(default=None, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True  # Set this model as Abstract

class Business(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    location = models.PointField(geography=True, default=Point(0.0, 0.0))



# class LikeType(Enum):
#     UPVOTE = 'upvote'
#     DOWNVOTE = 'downvote'
#
#
# class Restaurant(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)
#
#
# class Review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     review_text = models.TextField()
#
#
# class BusinessInfo(models.Model):
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     phone_number = models.CharField(max_length=255)
#     location = models.CharField(max_length=255)
#
#
# class Business(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#
#
# class ReviewLike(models.Model):
#     review = models.ForeignKey(Review, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     type = EnumField(LikeType, max_length=255)
#
#     class Meta:
#         unique_together = (("review", "user"),)
