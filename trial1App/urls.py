from django.urls import path
from . import views

urlpatterns = [
	path('trial', views.trial, name='trial'), 
	path('modelling', views.modelling, name='modelling'), 
	path('savePart', views.savePart, name='savePart'), 
	path('geomParameter', views.geomParameter, name='geomParameter'), 
	path('selectPart', views.selectPart, name='selectPart'), 
	path('reviewOrder', views.reviewOrder, name='reviewOrder'), 
	path('select_company', views.select_company, name='select_company'), 
	path('select_part', views.select_part, name='select_part'), 
	path('submit_order', views.submit_order, name='submit_order'), 
]
