from django import views
from django.contrib import admin
from django.urls import path
from django.views import View
from . import views
from django.conf.urls.static import static
from django.conf import settings
app_name="reviews"
urlpatterns = [
    path('',view=views.movie_list, name="review"),
    path('create/',view=views.movie_create,name='create'),
    path('<int:pk>/',view=views.movie_detail,name='detail'),
    path('<int:pk>/update',view=views.movie_update,name='update'),
    path('<int:pk>/delete',view=views.movie_delete,name='delete')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)