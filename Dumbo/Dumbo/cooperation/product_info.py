# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
import json

def product(request):
    return render(request, 'cooperation/product.html')