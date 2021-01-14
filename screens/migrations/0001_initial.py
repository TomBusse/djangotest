# Generated by Django 3.1.3 on 2021-01-10 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Screens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ScreenID', models.SlugField(max_length=15)),
                ('ScreenName', models.CharField(db_index=True, max_length=50)),
                ('Longitude', models.FloatField(default=51.3968255)),
                ('Latitude', models.FloatField(default=8.0638122)),
                ('StreetName', models.CharField(db_index=True, max_length=50)),
                ('ZIPCode', models.CharField(db_index=True, max_length=7)),
                ('Town', models.CharField(db_index=True, max_length=50)),
                ('ScreenWidth', models.IntegerField()),
                ('ScreenHeight', models.IntegerField()),
                ('XPitch', models.IntegerField()),
                ('YPitch', models.IntegerField()),
                ('XRes', models.IntegerField()),
                ('YRes', models.IntegerField()),
            ],
        ),
    ]
