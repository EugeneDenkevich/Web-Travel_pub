# Generated by Django 3.2 on 2023-08-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_owner_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseuser',
            name='was_changed',
            field=models.DateField(auto_now=True, verbose_name='Изменено'),
        ),
    ]