# Generated by Django 3.2 on 2023-06-29 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'О питании',
                'verbose_name_plural': 'О питании',
            },
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('byn', 'BYN'), ('rus', 'RUS'), ('usd', 'USD'), ('eur', 'EUR')], default='byn', max_length=4, verbose_name='Валюта')),
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
            name='RulesInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('was_changed', models.DateField(auto_now=True, verbose_name='Изменено')),
            ],
            options={
                'verbose_name': 'Правила',
                'verbose_name_plural': 'Правила',
            },
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_created=True, auto_now=True, null=True)),
                ('content', models.TextField(max_length=1000, verbose_name='Содержание')),
                ('rules', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rule', to='info.rulesinfo')),
            ],
            options={
                'verbose_name': 'Правило',
                'verbose_name_plural': 'Правила',
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
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('time', models.TimeField(verbose_name='Время')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Стоимость')),
                ('feeding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='info.feedinginfo')),
            ],
            options={
                'verbose_name': 'Приём пищи',
                'verbose_name_plural': 'Приёмы пищи',
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
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photo_dish', verbose_name='Фото')),
                ('feeding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='info.feedinginfo')),
            ],
            options={
                'verbose_name': 'Блюдо',
                'verbose_name_plural': 'Кухня',
            },
        ),
    ]