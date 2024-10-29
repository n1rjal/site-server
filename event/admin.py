# Register your models here.
from . import models
from django.contrib import admin


@admin.register(models.Event)
class EventModelAdmin(admin.ModelAdmin):
    list_filter = ["is_draft", "start_date", "price"]
    search_fields = ["slug", "title"]


admin.site.register(
    [
        models.Speaker,
        models.Schedule,
        models.HotTopic,
        models.EventLocation,
        models.EventType,
        models.EventImage,
    ]
)
