from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_view

app_name  = "services"

urlpatterns = [
    path("addcategory/", views.add_service_category, name="addcategory"),

]