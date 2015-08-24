from django.db import models
from django.contrib.auth.models import User


# Extending the default Django user model with Profile to allow addition of extra fields
class Profile(models.Model):
    user = models.OneToOneField(User)
    role = models.CharField(max_length=2000, blank=True)
    pledge = models.CharField(max_length=2000, blank=True)
    is_curator = models.BooleanField(default=False)
