# Generated by Django 3.1.3 on 2021-03-14 19:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('screens', '0012_auto_20210314_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='screens',
            name='CreationTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 14, 19, 30, 51, 314099, tzinfo=utc)),
        ),
    ]