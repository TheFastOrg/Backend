from django.contrib.gis.geos import Point
from django.db import models
from django.contrib.gis.db import models as gis_models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True  # Set this model as Abstract


class BusinessType(models.TextChoices):
    RESTAURANT = 'restaurant'


class BusinessStatus(models.TextChoices):
    DRAFT = 'draft'
    VERIFIED = 'verified'
    CLAIMED = 'claimed'
    DISCONTINUED = 'discontinued'


class BusinessContactType(models.TextChoices):
    PHONE = 'phone'
    FACEBOOK = 'facebook'
    WHATSAPP = 'whatsapp'
    INSTAGRAM = 'instagram'


class BusinessFeatureType(models.TextChoices):
    GENERAL = 'general'
    WIFI = 'wifi'
    PARKING = 'parking'


class Business(BaseModel):
    slug = models.CharField(unique=True, max_length=255)
    status = models.CharField(max_length=255, choices=BusinessStatus.choices)
    ar_name = models.CharField(max_length=255)
    en_name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=BusinessType.choices)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True, blank=True)
    address_line1 = models.CharField(max_length=255, null=True, blank=True)
    address_line2 = models.CharField(max_length=255, null=True, blank=True)
    location = gis_models.PointField(geography=True, default=Point(0.0, 0.0))


class BusinessWorkingHours(BaseModel):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    day = models.PositiveIntegerField()  # Starting from 1 = Monday
    opening_time = models.TimeField()
    closing_time = models.TimeField()


class BusinessContacts(BaseModel):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    contact_type = models.CharField(max_length=15, choices=BusinessContactType.choices)
    contact_value = models.CharField(max_length=255)


class Category(BaseModel):
    slug = models.CharField(unique=True, max_length=255)
    ar_name = models.CharField(max_length=255, null=True, blank=True)
    en_name = models.CharField(max_length=255, null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)


class BusinessCategories(BaseModel):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)


class Feature(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    ar_name = models.CharField(max_length=255)
    en_name = models.CharField(max_length=255)


class BusinessFeatures(BaseModel):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    feature = models.ForeignKey(Feature, on_delete=models.PROTECT)


class BusinessTags(BaseModel):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    tag = models.CharField(max_length=255)


class FeaturesCategory(BaseModel):
    ar_name = models.CharField(max_length=255)
    en_name = models.CharField(max_length=255)
