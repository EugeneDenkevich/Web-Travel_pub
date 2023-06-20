# Generated by Django 3.2 on 2023-06-12 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(max_length=1000, verbose_name='Адрес')),
                ('comment', models.TextField(max_length=1000, verbose_name='Комментарий')),
                ('geolocation', models.TextField(max_length=1000, verbose_name='Геолокация')),
            ],
            options={
                'verbose_name': 'Общая информация',
                'verbose_name_plural': 'Общая информация',
            },
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=256, verbose_name='Телефон')),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='info.info', verbose_name='phone')),
            ],
            options={
                'verbose_name': 'Телефон',
                'verbose_name_plural': 'Телефоны',
            },
        ),
        migrations.CreateModel(
            name='InfoSocial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Facebook', 'Facebook'), ('Instagram', 'Instagram')], max_length=256, verbose_name='Соц. сеть')),
                ('link', models.TextField()),
                ('info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='socials', to='info.info', verbose_name='info')),
            ],
            options={
                'verbose_name': 'Соц. сеть',
                'verbose_name_plural': 'Соц. сети',
            },
        ),
    ]
