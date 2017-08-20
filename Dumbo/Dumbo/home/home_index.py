# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import json

def home(request):
    return render(request, 'home/index.html')