from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_view

app_name  = "users"


urlpatterns = [

    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", auth_view.LoginView.as_view(template_name = "users/login.html"), name = 'login'),
    path("logout/", views.logmeout , name = 'logout'),
    path("profile/<int:userid>" , views.profile , name = 'profile'),
    path("userservice/<int:userid>", views.add_user_services, name = 'userservice'),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path( "services/delete/<int:service_id>/",views.delete_user_service, name="delete_user_service"),
    path("about/", views.about, name="about"),
    path("edit-profile-picture/", views.edit_profile_picture, name="edit_profile_picture" ),
    path('edit-contact-address/', views.edit_contact_address, name='edit_contact_address'),
    path('contactus/', views.edit_contact_address, name='contactus'),


]
