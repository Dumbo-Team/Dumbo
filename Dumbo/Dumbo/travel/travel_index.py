# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import json

from UserMapModel.models import UserMap
 
def index(request):
    context          = {}
    context['hello'] = 'Hello World!'

    visited_location = UserMap.objects.filter(user_id=1)
    data = []
    geoCoordMap = {}
    for item in visited_location:
        data.append({'name':item.name,'vlaue':20})
        geoCoordMap[item.name] = [item.longtitude, item.latitude]
        print item.name
    context['visited_location'] = json.dumps(data)
    context['geoCoordMap'] = json.dumps(geoCoordMap)

    return render(request, 'travel/index.html', context)