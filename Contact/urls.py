from django.urls import path
from . import views

app_name = 'Contact'
urlpatterns = [
    path('', views.home, name='contact'),
    path('Success/', views.success, name='success'),
]