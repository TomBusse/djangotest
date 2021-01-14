from django.urls import path

from screens import views

app_name = 'screens'
urlpatterns = [
    path('', views.screens_view, name='screens_view'),
]