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
        result = set(vessel.vessel_id for vessel in Vessel.objects.filter(point__intersects=zone.poly))
        return render(request, 'zone/index.html', context={
                'zone_id':zone_id,
                'result': result,
            }
        )
    return render(request, 'zone/index.html', context={'zone_id':''})