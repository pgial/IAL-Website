from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('modulo', views.modulo, name="modulo")
]