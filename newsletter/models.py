from django.db import models
from django.utils import timezone


# Create your models here.
class NewsletterSubscriber(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    email = models.EmailField(
        max_length=300,
        null=False,
        blank=False,
        unique=True,
        primary_key=True,
    )

    def __str__(self):
        return self.email
