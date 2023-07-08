from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=None, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True  # Set this model as Abstract


class Business(BaseModel):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    location = models.PointField(geography=True, default=Point(0.0, 0.0))

    @property
    def longitude(self):
        return self.location.x

    @property
    def latitude(self):
        return self.location.y
