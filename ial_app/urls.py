from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('modulo/<int:module>', views.modulo, name="modulo"),
    path('sobre', views.about, name='sobre')
]