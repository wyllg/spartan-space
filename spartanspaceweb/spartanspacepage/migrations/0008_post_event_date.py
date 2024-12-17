# Generated by Django 5.1.3 on 2024-11-17 11:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spartanspacepage', '0007_post_overview'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='event_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]