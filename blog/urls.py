from django.urls import path

from . import views


urlpatterns = [
    path('', views.blog),
    path('exemplo/', views.exemplo)
]
