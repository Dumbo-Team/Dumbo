"""Dumbo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from login import login_index
from travel import travel_index
from home import home_index
from cooperation import product_info
from technology import technology_index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', login_index.login),
    url(r'^home/$', home_index.home),
    url(r'^travel/$', travel_index.index),
    url(r'^travel/album$', travel_index.album),
    url(r'^product/$', product_info.product),
    url(r'^technology/$', technology_index.technology_info),
]
