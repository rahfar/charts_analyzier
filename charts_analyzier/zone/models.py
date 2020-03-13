from django.contrib.gis.db import models

# Create your models here.

class Zone(models.Model):
    zone_id = models.CharField(primary_key=True, db_index=True, max_length=100)
    poly = models.PolygonField()
