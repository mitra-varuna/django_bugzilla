from common import BugModel
from django.db import models


class User(BugModel):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


class Repository(BugModel):
    location = models.URLField()


class Project(BugModel):
    developer = models.ForeignKey(User, related_name='projects_in_developer_role')
    documenter = models.ForeignKey(User, related_name='projects_in_documenter_role')
    maintainer = models.ForeignKey(User, related_name='projects_in_maintainer_role')
    helper = models.ForeignKey(User, related_name='projects_in_helper_role')
    category = models.CharField(max_length=100)
    download_mirror = models.URLField()
    download_page = models.URLField()
    repository = models.ForeignKey(Repository)
    wiki = models.URLField()


