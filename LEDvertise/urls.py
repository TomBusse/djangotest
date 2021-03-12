"""LEDvertise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.urls import include, path

from locations.views import locations_view
#from screens.views import screens_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('main/', include('main.urls')),
    path('locations/', include('locations.urls')),
    path('screens/', include('screens.urls')),
    path('mains/', include('screens.urls')),
    path('', include('locations.urls')),
    #path('post/new/', views.newscreen, name='newscreen'),
]
