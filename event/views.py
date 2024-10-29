from rest_framework import viewsets
from . import serializers
from . import models
from rest_framework import permissions


class EventReadonlyViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.EventSerializer
    queryset = models.Event.objects.filter(is_draft=False)
    permission_classes = [
        permissions.AllowAny,
    ]
    lookup_field = "slug"
    lookup_url_kwarg = "slug"
