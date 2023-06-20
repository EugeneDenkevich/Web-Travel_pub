# Generated by Django 3.2 on 2023-06-12 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakfast_time', models.TimeField(default='09:00[:00[.000000]]', verbose_name='Время завтрака')),
                ('breakfast_cost', models.DecimalField(decimal_places=2, default='0.00', max_digits=6, verbose_name='Стоимость завтрака, руб')),
                ('dinner_time', models.TimeField(default='12:00[:00[.000000]]', verbose_name='Время обеда')),
                ('dinner_cost', models.DecimalField(decimal_places=2, default='0.00', max_digits=6, verbose_name='Стоимость обеда, руб')),
                ('supper_time', models.TimeField(default='18:00[:00[.000000]]', verbose_name='Время ужина')),
                ('supper_cost', models.DecimalField(decimal_places=2, default='0.00', max_digits=6, verbose_name='Стоимость ужина, руб')),
            ],
            options={
                'verbose_name': 'Информация о питании',
                'verbose_name_plural': 'Информация о питании',
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
