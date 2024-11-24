from django.db import models
from django.contrib.auth.models import AbstractUser

# Choices
ROLE_CHOICES = (
    ('Student', 'Student'),
    ('Counselor', 'Counselor'),
)

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

class User(AbstractUser):
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Student')
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, null=True, blank=True)
    
    # Set email as the primary login field
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # No need for 'username' because it's not required in this case

    def __str__(self):
        return self.email
