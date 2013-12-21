from django.db import models
from common import BugModel
from projects import User


class Priority(BugModel):
    label = models.CharField(max_length=100)


class Content(BugModel):
    src = models.URLField()
    language = models.CharField(max_length=50)
    body = models.TextField(blank=False)


class Post(BugModel):
    creator = models.ForeignKey(User, related_name='posts')
    when = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    content = models.OneToOneField(Content)