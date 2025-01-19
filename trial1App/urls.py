from django.urls import path
from . import views

urlpatterns = [
	path('', views.trial, name='home'), 
	path('modelling', views.modelling, name='modelling'), 
]
