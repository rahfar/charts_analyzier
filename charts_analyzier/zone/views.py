from django.shortcuts import render
from django.http import HttpResponse
from vessel.models import Vessel
from zone.models import Zone
from django.contrib.gis.geos import Point, MultiPoint

# Create your views here.

def zone(request):
    if request.method == 'POST':
        zone_id = request.POST['zone_id']
        zone = Zone.objects.get(zone_id__exact=zone_id)
        result = set()
        for v in Vessel.objects.values_list('vessel_id').distinct():
            all_points = MultiPoint([Point([x.longitude, x.latitude]) for x in Vessel.objects.filter(vessel_id__exact=v[0])])
            print(v[0])
            if all_points.intersects(zone.poly):
                result.add(v[0])
        return render(request, 'zone/index.html', context={
                'zone_id':zone_id,
                'result': result,
            }
        )
    return render(request, 'zone/index.html', context={'zone_id':''})