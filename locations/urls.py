from django.urls import path
from locations import views

app_name = 'locations'
urlpatterns = [
    path('', views.locations_view, name='locations_view'),
    path('/create_location', views.location_create_view, name='location_create_view'),
    path('locations/create_location', views.location_create_view, name='location_create_view'),
]


