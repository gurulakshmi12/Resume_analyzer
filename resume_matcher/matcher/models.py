from django.db import models

class Job(models.Model):
    description = models.TextField()

class Resume(models.Model):
    content = models.TextField()
