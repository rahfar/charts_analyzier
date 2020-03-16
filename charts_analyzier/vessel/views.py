from django.shortcuts import render
from django.http import HttpResponse
from vessel.models import Vessel
from zone.models import Zone
from django.contrib.gis.geos import MultiPoint
# Create your views here.

def vessel(request):
    if request.method == 'POST':
        vessel_id = request.POST['vessel_id']        
        all_points = MultiPoint([x.point for x in Vessel.objects.filter(vessel_id__exact=vessel_id)])
        result = set(zone.zone_id for zone in Zone.objects.filter(poly__intersects=all_points))
        return render(request, 'vessel/index.html', context={
                'vessel_id':vessel_id,
                'result': result,
            }
        )
    return render(request, 'vessel/index.html', context={'vessel_id':''})