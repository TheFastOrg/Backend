# your_app/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Business


class BusinessSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Business
    fields = {'id': serializers.Field(), 'user': serializers.Field(), 'user_token': serializers.Field(), 'email': serializers.Field(), 'name': serializers.Field()}