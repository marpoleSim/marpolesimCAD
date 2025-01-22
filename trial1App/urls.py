from django.urls import path
from . import views

urlpatterns = [
	path('', views.trial, name='home'), 
	path('modelling', views.modelling, name='modelling'), 
	path('savePart', views.savePart, name='savePart'), 
	path('geomParameter', views.geomParameter, name='geomParameter'), 
]
