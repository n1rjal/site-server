from rest_framework import serializers
from . import models


class NewsletterSubscriber(serializers.ModelSerializer):

    class Meta:
        model = models.NewsletterSubscriber
        fields = ["email"]
