from django.contrib import admin
from django.urls import path,include
from . import views
app_name='insta'
urlpatterns = [
    path('', views.list_insta,name="list_insta"),
    path('create/',views.create_insta,name="create"),
]