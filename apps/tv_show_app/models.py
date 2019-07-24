from __future__ import unicode_literals
from django.db import models
from datetime import datetime
# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "Title name should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Network name should be at least 3 characters"
        if len(postData["desc"]) > 0 and len(postData["desc"]) < 10:
            errors["description"] = "If description info is provided, it should be at least 10 characters"
        now = str(datetime.now())
        if postData["release_date"] >= now:
            errors["release_date"] = "Release date must be in the past"
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255, unique=True)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
    def __repr__(self):
        return f"<Show object: {self.title} ({self.id}) {self.network} {self.release_date} {self.description} {self.created_at} {self.updated_at}>"


