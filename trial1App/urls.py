from django.urls import path
from . import views

urlpatterns = [
	path('', views.trial, name='home'), 
	path('setHole', views.setHole, name='setHole'), 
]
