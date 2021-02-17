# Generated by Django 3.1.6 on 2021-02-13 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0005_auto_20210211_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('category', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Maps',
            },
        ),
    ]
