# Generated by Django 3.2 on 2023-08-20 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainments', '0005_alter_entertainmentprice_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainment',
            name='description_short',
            field=models.TextField(max_length=300, verbose_name='Короткое описание'),
        ),
    ]
