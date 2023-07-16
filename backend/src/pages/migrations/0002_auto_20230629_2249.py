# Generated by Django 3.2 on 2023-06-29 19:49

import config.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backphoto',
            name='photo_e',
            field=models.ImageField(default='/default/entertainment.jpg', upload_to='photo_pages', validators=[config.validators.validate_image_size], verbose_name='Фон Развлечения'),
        ),
        migrations.AlterField(
            model_name='backphoto',
            name='photo_h',
            field=models.ImageField(default='/default/houses.jpg', upload_to='photo_pages', validators=[config.validators.validate_image_size], verbose_name='Фон Домики'),
        ),
        migrations.AlterField(
            model_name='backphoto',
            name='photo_k',
            field=models.ImageField(default='/default/kitchen.jpg', upload_to='photo_pages', validators=[config.validators.validate_image_size], verbose_name='Фон Кухня'),
        ),
        migrations.AlterField(
            model_name='backphoto',
            name='photo_m',
            field=models.ImageField(default='/default/main.jpg', upload_to='photo_pages', validators=[config.validators.validate_image_size], verbose_name='Фон Главная'),
        ),
        migrations.AlterField(
            model_name='photomainpage',
            name='file',
            field=models.ImageField(blank=True, null=True, upload_to='photo_main_page', validators=[config.validators.validate_image_size], verbose_name='Файл'),
        ),
    ]