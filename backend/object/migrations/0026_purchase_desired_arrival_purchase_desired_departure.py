# Generated by Django 4.2 on 2023-05-14 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0025_entertaiment_price_entertaiment_price_desription_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='desired_arrival',
            field=models.DateField(default='2023-05-15'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='purchase',
            name='desired_departure',
            field=models.DateField(default='2023-05-20'),
            preserve_default=False,
        ),
    ]
