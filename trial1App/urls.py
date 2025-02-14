from django.urls import path
from . import views

urlpatterns = [
	path('trial', views.trial, name='trial'), 
	path('modelling', views.modelling, name='modelling'), 
	path('savePart', views.savePart, name='savePart'), 
	path('geomParameter', views.geomParameter, name='geomParameter'), 
	path('selectPart', views.selectPart, name='selectPart'), 
	path('select_part', views.select_part, name='select_part'), 
	path('submit_order', views.submit_order, name='submit_order'), 
	path('user_review_order', views.user_review_order, name='user_review_order'), 
	path('company_review_order', views.company_review_order, name='company_review_order'), 
	path('download_order', views.download_order, name='download_order'), 
	path('ordered_part', views.ordered_part, name='ordered_part'), 
	path('downloadSTL', views.downloadSTL, name='downloadSTL'), 
]
