from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views


app_name="Idea"
urlpatterns = [
    path('',views.idea_list,name="list"),
    path('<int:pk>/',views.idea_detail,name="detail"),
    path('create/',views.idea_create,name='create'),
    path('<int:pk>/fix',views.idea_fix,name='fix'),
    path('<int:pk>/delete',views.idea_delete,name="delete"),
    path('dev_list/',views.dev_list,name="dev_list"),
    path('dev_create/',views.dev_create,name="dev_create"),
    path('<int:pk>/dev_detail/',views.dev_detail,name="dev_detail"),
    path('<int:pk>/dev_delete',views.dev_delete,name="dev_delete"),
    path('<int:pk>/dev_fix',views.dev_fix,name="dev_fix"),
    path('button_ajax/',views.button_ajax,name='button_ajax')
]

