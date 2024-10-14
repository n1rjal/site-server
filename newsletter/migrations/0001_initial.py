# Generated by Django 5.1.1 on 2024-10-14 09:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSubscriber',
            fields=[
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=300, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]