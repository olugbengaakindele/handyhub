from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_view
from django.contrib.auth.views import LoginView, LogoutView

app_name  = "users"

urlpatterns = [

    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path("logout/", views.logmeout , name = 'logout'),
    path("profile/" , views.profile , name = 'profile'),
    path("userservice", views.add_user_services, name = 'userservice'),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path( "services/delete/<int:service_id>/",views.delete_user_service, name="delete_user_service"),
    path("about/", views.about, name="about"),
    path("edit-profile-picture/", views.edit_profile_picture, name="edit_profile_picture" ),
    path('edit-contact-address/', views.edit_contact_info, name='edit_contact_info'),
    path('edit-address-info/', views.edit_address_info, name='edit_address_info'),
    path('contactus/', views.contactus, name='contactus'),
    path('edit-service-areas/', views.edit_service_areas, name='edit_service_areas'),
    path("service-areas/delete/<int:area_id>/", views.delete_service_area_confirm, name="delete_service_area"),

]
