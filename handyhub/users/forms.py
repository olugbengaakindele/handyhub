from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import UserProfile 
User = get_user_model()



#  this registers a user to the user modesl. This is thes basic reg needed to create a profile.

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "password1": forms.PasswordInput(attrs={"class": "form-control"}),
            "password2": forms.PasswordInput(attrs={"class": "form-control"}),
        }

    # Make sure email is unique
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email




# This is to update user profile
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            "user_firstname",
            "user_last_name",
            "user_preferred_name",
            "user_business_name",
            "user_profile_image",
            "user_address_line1",
            "user_address_line2",
            "user_city",
            "user_province",
            "user_postal_code",
            "user_website",
        ]

        # CLEAN LABELS
        labels = {
            "user_firstname": "First Name",
            "user_last_name": "Last Name",
            "user_preferred_name": "Preferred Name",
            "user_business_name": "Business Name",
            "user_profile_image": "Profile Image",
            "user_address_line1": "Address Line 1",
            "user_address_line2": "Address Line 2",
            "user_city": "City",
            "user_province": "Province",
            "user_postal_code": "Postal Code",
            "user_website": "Website",
        }

        widgets = {
            "user_firstname": forms.TextInput(attrs={"class": "form-control"}),
            "user_last_name": forms.TextInput(attrs={"class": "form-control"}),
            "user_preferred_name": forms.TextInput(attrs={"class": "form-control"}),
            "user_business_name": forms.TextInput(attrs={"class": "form-control"}),
            "user_profile_image": forms.FileInput(attrs={"class": "form-control"}),
            "user_address_line1": forms.TextInput(attrs={"class": "form-control"}),
            "user_address_line2": forms.TextInput(attrs={"class": "form-control"}),
            "user_city": forms.TextInput(attrs={"class": "form-control"}),
            "user_province": forms.Select(attrs={"class": "form-control"}),
            "user_postal_code": forms.TextInput(attrs={"class": "form-control"}),
            "user_website": forms.URLInput(attrs={"class": "form-control"}),
        }
