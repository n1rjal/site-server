from . import models, serializers
from rest_framework.generics import CreateAPIView


# Create your views here.
class NewsletterCreateView(CreateAPIView):
    queryset = models.NewsletterSubscriber.objects.all()
    serializer_class = serializers.NewsletterSubscriber
