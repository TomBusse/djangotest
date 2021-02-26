from django.urls import path

from screens import views
print ("screens/urls.py")
app_name = 'screens'
urlpatterns = [
    path('', views.screens_view, name='screens_view'),
    path('screens/new/', views.postscreen, name='postscreen'),
    path('screens/', views.screens_view, name='screens_view'),
    path('screens/screen/<int:pk>/', views.screens_view, name='screens_view'),
]