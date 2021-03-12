from django.urls import path

from . import views

print("main/urls.py")
app_name = 'main'
urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('main/', views.main_view, name='main_view'),
]
