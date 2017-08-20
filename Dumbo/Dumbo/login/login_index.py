# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import json

def login(request):
    return render(request, 'login/login.html')