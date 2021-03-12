from django.urls import path

from . import views

urlpatterns = [
    path('', views.locations_view, name='locations_view'),
    path('locations/', views.locations_view, name='locations_view'),
]


