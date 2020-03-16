from django.contrib.gis.db import models

# Create your models here.

class Vessel(models.Model):
    timestamp = models.DateTimeField()
    vessel_id = models.IntegerField(db_index=True)
    vessel_name = models.TextField()
    point = models.PointField()