from django.urls import path
from future_de import views

app_name = 'future_de'
urlpatterns = [
    path('', views.future_de_view, name='future_de_view'),
]
