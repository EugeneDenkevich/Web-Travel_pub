# Generated by Django 3.2 on 2023-08-04 02:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0010_alter_purchase_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='count_adult',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='count of the adults'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='count_kids',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(20)], verbose_name='count of the children'),
        ),
    ]
