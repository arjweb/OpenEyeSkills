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
    visible = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_modified = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    # TODO Add method to show the curator

    # TODO Add method to calculate days since resource added


class Level(models.Model):
    level_desc = models.CharField(max_length=10)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_modified = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.level_desc


class JobType(models.Model):
    job = models.CharField(max_length=40)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_modified = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.job


class CatalogueItem(models.Model):
    title = models.CharField(max_length=80)
    # TODO check database max lengths for text fields
    description = models.CharField(max_length=2000, blank=True)
    topic_area = models.ForeignKey(TopicArea)
    level = models.ForeignKey(Level)
    link = models.CharField(max_length=255)
    discovered_by = models.ForeignKey(User)
    what_learn = models.CharField(max_length=2000, blank=True)
    how_apply = models.CharField(max_length=2000, blank=True)
    relevant_to = models.ManyToManyField(JobType)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_modified = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title

    def full_name(self):
        # Fetches full name of the discovered_by linked user
        return self.discovered_by.get_full_name()
