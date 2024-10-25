from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=700, null=False, blank=False)
    answer = models.CharField(max_length=700, null=False, blank=False)
    position = models.IntegerField(
        null=False,
        blank=False,
        validators=[MinValueValidator(1)],
    )

    def __str__(self) -> str:
        return self.question
