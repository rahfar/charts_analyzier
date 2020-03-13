import csv
import glob
import datetime
import time
import os
from django.utils import timezone
from vessel.models import Vessel

file_path = os.path.join(os.path.dirname(__file__), "charts_prj_data/charts_prj_vessel_tracks/*.csv")

start = time.perf_counter()
for path in glob.glob(file_path):
    tic = time.perf_counter()
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader) # skip first line
        obj_list = []
        for row in reader:
            obj_list.append(Vessel(
                timestamp = datetime.datetime.fromtimestamp(int(row[0]), timezone.get_current_timezone()),
                longitude = float(row[1]),
                latitude = float(row[2]),
                vessel_id = int(row[3]),
                vessel_name = row[4]
            ))
        Vessel.objects.bulk_create(obj_list)
    toc = time.perf_counter()
    print(path, f'proceded in {datetime.timedelta(seconds=int(toc-tic))}')
stop = time.perf_counter()
print(f'TOTAL {datetime.timedelta(seconds=int(stop-start))}')
