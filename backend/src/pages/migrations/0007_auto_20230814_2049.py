# Generated by Django 3.2 on 2023-08-14 17:49

import config.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20230720_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backphoto',
            name='photo_e',
            field=models.ImageField(blank=True, null=True, upload_to='photo_pages', validators=[config.validators.validate_image_size, config.validators.validate_name], verbose_name='Фон Развлечения'),
        ),
        migrations.AlterField(
            model_name='backphoto',
            name='photo_h',
            field=models.ImageField(blank=True, null=True, upload_to='photo_pages', validators=[config.validators.validate_image_size, config.validators.validate_name], verbose_name='Фон Домики'),
        ),
        migrations.AlterField(
            model_name='backphoto',
            name='photo_k',
            field=models.ImageField(blank=True, null=True, upload_to='photo_pages', validators=[config.validators.validate_image_size, config.validators.validate_name], verbose_name='Фон Кухня'),
        ),
        migrations.AlterField(
            model_name='backphoto',
            name='photo_m',
            field=models.ImageField(blank=True, null=True, upload_to='photo_pages', validators=[config.validators.validate_image_size, config.validators.validate_name], verbose_name='Фон Главная'),
        ),
    ]
