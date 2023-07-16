# Generated by Django 3.2 on 2023-06-29 19:49

import config.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoentertainment',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='photo_entertainment', validators=[config.validators.validate_image_size], verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='photogalery',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='photo_galery', validators=[config.validators.validate_image_size], verbose_name='Файл'),
        ),
        migrations.AlterField(
            model_name='photonearestplace',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='photo_nearest_places', validators=[config.validators.validate_image_size], verbose_name='Файл'),
        ),
    ]
