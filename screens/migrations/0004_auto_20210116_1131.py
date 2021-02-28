# Generated by Django 3.1.3 on 2021-01-16 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0003_auto_20210110_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screens',
            name='Latitude',
        ),
        migrations.RemoveField(
            model_name='screens',
            name='Longitude',
        ),
        migrations.RemoveField(
            model_name='screens',
            name='StreetName',
        ),
        migrations.RemoveField(
            model_name='screens',
            name='Town',
        ),
        migrations.RemoveField(
            model_name='screens',
            name='ZIPCode',
        ),
        migrations.AddField(
            model_name='screens',
            name='IsMobile',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='screens',
            name='LocationCode',
            field=models.SlugField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='screens',
            name='ScreenCode',
            field=models.SlugField(max_length=20, unique=True),
        ),
    ]
