# Generated by Django 5.1.3 on 2024-12-17 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spartanspacepage', '0010_remove_post_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
