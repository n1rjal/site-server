from rest_framework import serializers
from . import models


class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventImage
        fields = "__all__"


class EventLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EventLocation
        fields = "__all__"


class HotTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HotTopic
        fields = "__all__"


class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Speaker
        fields = "__all__"


class ScheduleSerializer(serializers.ModelSerializer):
    speakers = SpeakerSerializer(many=True)

    class Meta:
        model = models.Schedule
        fields = "__all__"


class EventSerializer(serializers.ModelSerializer):
    event_type = serializers.StringRelatedField()
    location = EventLocationSerializer()
    hot_topics = serializers.StringRelatedField(many=True)
    schedules = ScheduleSerializer(many=True)
    images = serializers.SerializerMethodField(read_only=True)

    def get_images(self, obj):
        images = []
        for img in obj.event_images.filter(published=True).order_by(
            "position"
        ):
            images.append(
                {
                    "caption": img.caption,
                    "images": img.image.url,
                    "created_at": img.created_at,
                }
            )

        return images

    class Meta:
        model = models.Event
        fields = "__all__"
