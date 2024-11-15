# Generated by Django 5.1.1 on 2024-11-15 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("event", "0004_alter_event_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="schedule",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/%Y/%m/%d/schedules/"
            ),
        ),
        migrations.AddField(
            model_name="speaker",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/%Y/%m/%d/speakers/"
            ),
        ),
        migrations.AlterField(
            model_name="eventimage",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/%Y/%m/%d/event_images"
            ),
        ),
    ]