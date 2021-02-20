# Generated by Django 3.1.6 on 2021-02-20 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(help_text='Every portfolio needs a heading. Whats your going to be?', max_length=100)),
                ('description', models.TextField(help_text='Describe the type of projects you are mainly involved in.')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Members Portfolio',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('summary', models.TextField(help_text='What was the project all about? Explain in detail')),
                ('image', models.ImageField(default='default.png', upload_to='projects')),
                ('url', models.URLField()),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='careers.portfolio')),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
    ]
