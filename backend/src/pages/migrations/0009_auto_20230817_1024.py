# Generated by Django 3.2 on 2023-08-17 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_alter_policyagreement_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='backphoto',
            name='was_changed',
            field=models.DateField(auto_now=True, verbose_name='Изменено'),
        ),
        migrations.AddField(
            model_name='mainpage',
            name='was_changed',
            field=models.DateField(auto_now=True, verbose_name='Изменено'),
        ),
        migrations.AddField(
            model_name='policyagreement',
            name='was_changed',
            field=models.DateField(auto_now=True, verbose_name='Изменено'),
        ),
    ]