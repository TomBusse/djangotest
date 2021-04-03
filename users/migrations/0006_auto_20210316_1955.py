# Generated by Django 3.1.3 on 2021-03-16 19:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210316_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='CreationTime',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 16, 19, 55, 22, 655894, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='users',
            name='State',
            field=models.CharField(blank=True, db_index=True, max_length=50),
        ),
    ]
