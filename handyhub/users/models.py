from django.db import models
from django.contrib.auth import get_user_model
from services.models import SubCategory, ServiceCategory
import uuid
import os


User = get_user_model()

def profile_image_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('profile_pictures', filename)




# Create your models here.
class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    # Basic info
    user_firstname = models.CharField(max_length=150)
    user_last_name = models.CharField(max_length=150)
    user_preferred_name = models.CharField(max_length=150)
    user_business_name = models.CharField(max_length=200, blank=True, null=True)
    user_profile_image = models.ImageField(default="no_profile_picture.jpg", upload_to= profile_image_path)

    
    # 📞 Contact phone numbers
    user_primary_phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Primary contact phone number"
    )
    user_secondary_phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Secondary contact phone number"
    )
    user_business_phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Business contact phone number"
    )
    
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
    
class UserProvince(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)  # e.g. AB, ON

    def __str__(self):
        return self.name

class UserService(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "services")
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "subcategory")  # prevents duplicates

    def __str__(self):
        return f"{self.user} - {self.subcategory.name}"