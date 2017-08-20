# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import json

def technology_info(request):
    return render(request, 'technology/index.html')