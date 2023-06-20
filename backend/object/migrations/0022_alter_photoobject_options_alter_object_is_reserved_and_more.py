# Generated by Django 4.2 on 2023-05-06 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0021_object_is_reserved_alter_object_created_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photoobject',
            options={'verbose_name': 'Фото', 'verbose_name_plural': 'Фото'},
        ),
        migrations.AlterField(
            model_name='object',
            name='is_reserved',
            field=models.BooleanField(default=False, verbose_name='Занят'),
        ),
        migrations.AlterField(
            model_name='object',
            name='pers_num',
            field=models.IntegerField(verbose_name='Вместимость'),
        ),
    ]
