# Generated by Django 3.1.3 on 2021-02-28 09:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0007_screens_creationtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screens',
            name='CreationTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 2, 28, 9, 14, 34, 267102, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='screens',
            name='LocationCode',
            field=models.CharField(db_index=True, max_length=20, null=True),
        ),
    ]
