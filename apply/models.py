from django.db import models
# from listings.models import PostJob


# Create your models here.
class ApplicantForm(models.Model):
    job = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    mobile = models.CharField(max_length=15)
    education = models.CharField(max_length=50)
    exp = models.CharField(max_length=50)
    resume = models.FileField(upload_to="resume/%Y/%m/%d/")

    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.ForeignKey(ApplicantForm, on_delete=models.CASCADE, null=False)
    reviewd = models.BooleanField(default=False)
    ratings = models.CharField(max_length=2, default="0")
    remarks = models.TextField(blank=True)

    def __str__(self):
        return self.name.name
