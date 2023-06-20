# Generated by Django 4.2 on 2023-05-03 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0020_alter_object_description_long_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='object',
            name='is_reserved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='object',
            name='created_date',
            field=models.DateField(auto_now_add=True, verbose_name='Дата добавления'),
        ),
    ]
