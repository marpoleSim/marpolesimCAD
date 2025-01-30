from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import TemplateView

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name="home"),  
    path('user_cover_page', views.user_cover_page, name="user_cover_page"),  
    path('', views.home, name="home"),  
    path('', include("accounts.urls")), 
    path('', include('trial1App.urls')),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)

