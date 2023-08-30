# Generated by Django 3.2 on 2023-08-08 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0012_delete_feature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bed',
            name='type',
            field=models.CharField(choices=[('sgb', 'Single Bed'), ('dbb', 'Double Bed'), ('qsb', 'Queen SizeBed'), ('ksb', 'King SizeBed'), ('exb', 'Extra Bed'), ('crb', 'Crib')], max_length=40, verbose_name='Кровать'),
        ),
        migrations.AlterField(
            model_name='objectfeature',
            name='type',
            field=models.CharField(choices=[('Internet', 'Интернет'), ('Shower', 'Душ'), ('Kitchen', 'Кухня'), ('TV', 'Телевизор'), ('Fridge', 'Холодильник'), ('Conditioner', 'Кондеционер'), ('Playground', 'Детская площадка'), ('Brazier', 'Мангал')], max_length=256, verbose_name='Тип услуги'),
        ),
    ]