# Generated by Django 3.1.3 on 2021-03-14 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations',
            name='Code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='locations',
            name='Name',
            field=models.CharField(max_length=50),
        ),
    ]