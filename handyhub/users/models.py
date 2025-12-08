from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # Basic info
    user_firstname = models.CharField(max_length=150)
    user_last_name = models.CharField(max_length=150)
    user_preferred_name = models.CharField(max_length=150)
    user_business_name = models.CharField(max_length=200, blank=True, null=True)
    user_profile_image = models.ImageField(default="no_profile_picture.jpg", upload_to= "profile_pictures")

    # Canadian Address Fields
    user_address_line1 = models.CharField("Address Line 1", max_length=255)
    user_address_line2 = models.CharField("Address Line 2", max_length=255, blank=True, null=True)
    user_city = models.CharField(max_length=100)
    user_province = models.CharField(
        max_length=50,
        choices=[
            ("AB", "Alberta"),
            ("BC", "British Columbia"),
            ("MB", "Manitoba"),
            ("NB", "New Brunswick"),
            ("NL", "Newfoundland and Labrador"),
            ("NS", "Nova Scotia"),
            ("NT", "Northwest Territories"),
            ("NU", "Nunavut"),
            ("ON", "Ontario"),
            ("PE", "Prince Edward Island"),
            ("QC", "Quebec"),
            ("SK", "Saskatchewan"),
            ("YT", "Yukon"),
        ]
    )
    user_postal_code = models.CharField(max_length=10)

    # Website
    user_website = models.URLField(blank=True, null=True)

    # Timestamps
    user_created_at = models.DateTimeField(auto_now_add=True)
    user_updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user_firstname})"