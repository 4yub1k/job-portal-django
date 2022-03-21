from django.db import models
from datetime import datetime

class PostJob(models.Model):
    job = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    job_published = models.BooleanField(default=True)
    post_date= models.DateTimeField(default=datetime.now, blank=True)
    last_date= models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.job