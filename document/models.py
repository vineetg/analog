from django.db import models

# Create your models here.
class Document(models.Model):
    uri = models.URLField()
    recurse = models.BooleanField(default=True)
    date_created = models.DateTimeField()
    date_updated = models.DateTimeField()
