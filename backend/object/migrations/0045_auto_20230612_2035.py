# Generated by Django 3.2 on 2023-06-12 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0044_auto_20230612_2028'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rule',
        ),
        migrations.DeleteModel(
            name='RulesInfo',
        ),
    ]
