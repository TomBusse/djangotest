# Generated by Django 3.1.3 on 2021-03-16 12:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0014_auto_20210314_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screens',
            name='CreationTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 12, 18, 7, 794855, tzinfo=utc)),
        ),
    ]
