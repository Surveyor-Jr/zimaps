# Generated by Django 3.1.6 on 2021-02-20 16:20

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('careers', '0006_service_slug'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Service',
            new_name='Services',
        ),
    ]
