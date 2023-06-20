# Generated by Django 3.2 on 2023-06-16 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('object', '0050_purchase_was_object'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='object',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='object.object', verbose_name='Домик'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='was_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='was_purchases', to='object.object', verbose_name='Домик в заказе'),
        ),
    ]
