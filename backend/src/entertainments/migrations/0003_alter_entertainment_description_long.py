# Generated by Django 3.2 on 2023-07-12 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entertainments', '0002_auto_20230629_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entertainment',
            name='description_long',
            field=models.TextField(blank=True, null=True, verbose_name='Полное описание'),
        ),
    ]