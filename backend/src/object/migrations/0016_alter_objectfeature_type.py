# Generated by Django 3.2 on 2023-08-21 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0015_auto_20230817_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='objectfeature',
            name='type',
            field=models.CharField(choices=[('Internet', 'Интернет'), ('Wifi', 'Бесплатный Wi-Fi'), ('Terrace', 'Терасса'), ('Patio', 'Патио'), ('Balcony', 'Балкон'), ('Dishes', 'Посуда'), ('Hair dryer', 'Фен'), ('Iron', 'Утюг'), ('Washing machine', 'Стиральная машина'), ('Gas stove', 'Газовая плита'), ('Microwave', 'Микроволновая печь'), ('Dishwasher', 'Посудомоечная машина'), ('Shower / bath', 'Душ / ванна'), ('Furniture for babies', 'Мебель для грудных детей'), ('Smoking indoors is prohibited', 'Курение в помещении запрещено'), ('Electric stove', 'Электроплита'), ('Personal pier', 'Личный пирс'), ('Shower', 'Душ'), ('Kitchen', 'Кухня'), ('TV', 'Телевизор'), ('Fridge', 'Холодильник'), ('Conditioner', 'Кондиционер'), ('Playground', 'Детская площадка'), ('Brazier', 'Мангал')], max_length=256, verbose_name='Тип услуги'),
        ),
    ]
