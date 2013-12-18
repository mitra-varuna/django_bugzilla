from django.contrib import admin
from bugs.models import Repository, Project, User

for model in [Repository, Project, User]:
    admin.site.register(model)
# Register your models here.
