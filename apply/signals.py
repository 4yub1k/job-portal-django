from django.db.models.signals import post_save
from .models import Review
from django.dispatch import receiver
from .models import ApplicantForm


@receiver(post_save, sender=ApplicantForm)
def create_review(sender, instance, created, **kwargs):
    if created:
        Review.objects.create(name=instance)
