# Generated by Django 3.1.6 on 2021-02-11 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector', '0002_provinces'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provinces',
            name='engtype_1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='provinces',
            name='nl_name_1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='provinces',
            name='type_1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='provinces',
            name='varname_1',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
