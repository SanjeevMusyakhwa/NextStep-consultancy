from django.db import models
from django.contrib.auth.models import AbstractUser

# Choices for gender
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

# Choices for roles
ROLE_CHOICES = (
    ('Student', 'Student'),
    ('Counselor', 'Counselor'),
)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Student')  # Set role field instead of is_student / is_counselor

    # Set email as the primary login field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Only 'username' is required for admin creation

    def __str__(self):
        return self.email
