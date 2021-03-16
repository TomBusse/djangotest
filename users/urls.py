from django.urls import path
from users import views

app_name = 'users'
urlpatterns = [
    path('', views.create_user_view, name='create_user_view'),
    path('create_user/', views.create_user_view, name='create_user_view'),

]


