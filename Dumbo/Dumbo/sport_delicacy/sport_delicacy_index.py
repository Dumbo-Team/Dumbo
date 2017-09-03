# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from MoodTalkModel.models import MoodTalk
import json

def test(request):
    return render(request, 'sport_delicacy/sport_delicacy.html')
def test_dynamic(request):
	data_list = []
	moods = MoodTalk.objects.all()
	for mood in moods:
		single_data = {}
		single_data['title'] = mood.title
		single_data['datatime'] = mood.datetime
		single_data['paragraph'] = mood.paragraph
		single_data['img_paths'] = mood.image_list
		data_list.append(single_data)
	data_dict = {'datas':data_list}
	return JsonResponse(data_dict)