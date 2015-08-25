from django.db import models
from django.contrib.auth.models import User


# Extending the default Django user model with Profile to allow addition of extra fields
class Profile(models.Model):
    user = models.OneToOneField(User)
    role = models.CharField(max_length=2000, blank=True)
    pledge = models.CharField(max_length=2000, blank=True)
    is_curator = models.BooleanField(default=False)


class TopicArea(models.Model):
    name = models.CharField(max_length=40)
    # TODO check database max lengths for text fields
    definition = models.CharField(max_length=2000, blank=True)
    curator = models.ForeignKey(User)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_modified = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    # TODO Add method to show the curator

    # TODO Add method to calculate days since resource added
