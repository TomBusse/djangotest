from django.urls import path

from screens import views
print ("screens/urls.py")
app_name = 'screens'
urlpatterns = [
    path('', views.screens_view, name='screens_view'),
    path('screens/new/', views.postscreen, name='postscreen'),
    path('screens/', views.screens_view, name='screens_view'),
    path('info/', views.screen_info, name='screen_info'),
    path('<int:pk>/', views.screens_info, name='screens_info'),
]