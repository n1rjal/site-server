from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from . import serializers
from . import models


# Create your views here.
class FaqViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = models.Faq.objects.filter().order_by("position")
    serializer_class = serializers.FaqSerializer
