# Generated by Django 4.1.1 on 2022-09-14 05:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('remi', '0003_alter_product_price_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='product_type', to='remi.producttype'),
        ),
        migrations.AlterField(
            model_name='productspecificationvalue',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specification', to='remi.product'),
        ),
    ]
