from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Ticket(models.Model):
    issue_summary = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    issue_description = models.TextField()
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    target_resolution = models.DateTimeField(default=timezone.now)
    priority = models.CharField(max_length=30)
    issue_status = models.CharField(max_length=30)

    def __str__(self):
        return self.issue_summary