import os
import django
import csv
import glob
import datetime
import time
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'charts_analyzier.settings')
django.setup()

from zone.models import Zone
from vessel.models import Vessel
from django.utils import timezone
from django.contrib.gis.geos import Polygon, Point

# LOAD ZONE

zone_list = []
with open('data/charts_prj_data/geo_zones.json', 'r') as f:
    data = json.load(f)
    for zone in data.keys():
        zone_list.append(
            Zone(
                zone_id = zone,
                poly = Polygon(data[zone] + [data[zone][0]])
            )
        )
Zone.objects.bulk_create(zone_list)

# LOAD VESSEL

start = time.perf_counter()
for path in glob.glob('data/charts_prj_data/charts_prj_vessel_tracks/*.csv'):
    tic = time.perf_counter()
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader) # skip first line
        vessel_list = []
        for row in reader:
            vessel_list.append(Vessel(
                timestamp = datetime.datetime.fromtimestamp(int(row[0]), timezone.get_current_timezone()),
                longitude = float(row[1]),
                latitude = float(row[2]),
                vessel_id = int(row[3]),
                vessel_name = row[4]
            ))
        Vessel.objects.bulk_create(vessel_list)
    toc = time.perf_counter()
    print(path, f'proceded in {datetime.timedelta(seconds=int(toc-tic))}')
stop = time.perf_counter()
print(f'TOTAL {datetime.timedelta(seconds=int(stop-start))}')
