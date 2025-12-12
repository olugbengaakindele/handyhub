from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import UserProfile 
import re


User = get_user_model()


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

    # Validate unique email
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("A user with this email already exists.")
        return email

    # THE CORRECT PLACE FOR PASSWORD VALIDATION
    def clean_password2(self):
        pw1 = self.cleaned_data.get("password1")
        pw2 = self.cleaned_data.get("password2")

        # First ensure Django still checks matching
        if pw1 and pw2 and pw1 != pw2:
            raise forms.ValidationError("Passwords do not match.")

        # Length rule
        if len(pw1) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")

        # At least 1 letter
        if not re.search(r"[A-Za-z]", pw1):
            raise forms.ValidationError("Password must contain at least one letter.")

        # At least 1 number
        if not re.search(r"[0-9]", pw1):
            raise forms.ValidationError("Password must contain at least one number.")

        return pw2



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
