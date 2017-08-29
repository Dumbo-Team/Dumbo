# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import json

def test(request):
    return render(request, 'sport_delicacy/sport_delicacy.html')