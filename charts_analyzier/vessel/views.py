from django.shortcuts import render
from django.http import HttpResponse
from vessel.models import Vessel
from zone.models import Zone
from django.contrib.gis.geos import Point, MultiPoint
# Create your views here.

def vessel(request):
    if request.method == 'POST':
        vessel_id = request.POST['vessel_id']
        result = set()
        all_points = MultiPoint([Point([x.longitude, x.latitude]) for x in Vessel.objects.filter(vessel_id__exact=vessel_id)])
        for zone in Zone.objects.all():
            if all_points.intersects(zone.poly):
                result.add(zone.zone_id)
        return render(request, 'vessel/index.html', context={
                'vessel_id':vessel_id,
                'result': result,
            }
        )
    return render(request, 'vessel/index.html', context={'vessel_id':''})