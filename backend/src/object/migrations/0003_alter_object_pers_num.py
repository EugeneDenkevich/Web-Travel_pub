# Generated by Django 3.2 on 2023-06-29 20:14

import config.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0002_alter_photoobject_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='pers_num',
            field=models.IntegerField(verbose_name='Вместимость'),
        ),
    ]
