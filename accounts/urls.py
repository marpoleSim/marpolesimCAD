from django.urls import path
from . import views

urlpatterns = [
    path("user_login/", views.user_login_view, name="user_login"),
    path("user_signup/", views.user_signup, name="user_signup"),
    path("company_login/", views.company_login_view, name="company_login"),
    path("company_signup/", views.company_signup, name="company_signup"),
    path("customer_info/", views.customer_info_view, name="customer_info"),
]

