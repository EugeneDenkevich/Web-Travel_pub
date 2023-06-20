# Generated by Django 4.2 on 2023-05-17 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0030_galery_alter_bed_object_id_photogalery'),
    ]

    operations = [
        migrations.CreateModel(
            name='NearestPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Ближайшие места',
            },
        ),
        migrations.AlterModelOptions(
            name='galery',
            options={'verbose_name': 'Галерея', 'verbose_name_plural': 'Галереи'},
        ),
        migrations.AlterField(
            model_name='galery',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Название'),
        ),
        migrations.CreateModel(
            name='PhotoNearestPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(blank=True, null=True, upload_to='photo_nearest_places', verbose_name='Файл')),
                ('places', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='object.nearestplace')),
            ],
            options={
                'verbose_name': 'Фото ближайшего места',
                'verbose_name_plural': 'Фото ближайших мест',
            },
        ),
    ]
