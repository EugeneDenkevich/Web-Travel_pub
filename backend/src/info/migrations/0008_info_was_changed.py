# Generated by Django 3.2 on 2023-08-17 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_auto_20230802_0448'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='was_changed',
            field=models.DateField(auto_now=True, verbose_name='Изменено'),
        ),
    ]