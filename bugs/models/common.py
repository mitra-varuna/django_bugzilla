from django.db import models

class BugModel(models.Model):
    class Meta:
        app_label = 'bugs'
        abstract = True