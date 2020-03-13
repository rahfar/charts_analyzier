import json
import os
from zone.models import Zone
from django.contrib.gis.geos import Polygon, Point

file_path = os.path.join(os.path.dirname(__file__), "charts_prj_data/geo_zones.json")

obj_list = []
with open(file_path, 'r') as f:
    data = json.load(f)
    for zone in data.keys():
        obj_list.append(
            Zone(
                zone_id = zone,
                poly = Polygon(data[zone] + [data[zone][0]])
            )
        )
Zone.objects.bulk_create(obj_list)
