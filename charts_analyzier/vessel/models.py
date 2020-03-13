from django.db import models

# Create your models here.

class Vessel(models.Model):
    timestamp = models.DateTimeField()
    vessel_id = models.IntegerField(db_index=True)
    vessel_name = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()