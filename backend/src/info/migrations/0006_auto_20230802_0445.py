# Generated by Django 3.2 on 2023-08-02 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0005_auto_20230712_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='geolocation',
        ),
        migrations.AddField(
            model_name='info',
            name='heigth',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Геолокация'),
        ),
        migrations.AddField(
            model_name='info',
            name='width',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Геолокация'),
        ),
    ]
