# Generated by Django 3.2 on 2023-07-21 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_baseuser_is_staff'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='baseuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'owner',
                'verbose_name_plural': 'owner',
            },
        ),
    ]
