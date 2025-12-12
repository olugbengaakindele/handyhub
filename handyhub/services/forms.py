from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
import re
from django import forms
from .models import ServiceCategory

User = get_user_model()

# forms.py


class ServiceCategoryForm(forms.ModelForm):
    class Meta:
        model = ServiceCategory
        fields = ["name"]  # only the name should be entered by the admin

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full p-3 border border-gray-300 rounded-lg",
                "placeholder": "Enter category name"
            })
        }