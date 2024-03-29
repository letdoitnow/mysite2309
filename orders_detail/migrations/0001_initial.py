# Generated by Django 4.2.8 on 2024-01-29 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0001_initial'),
        ('product', '0007_productmodel_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdersDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('orders', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.ordersmodel')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.productmodel')),
            ],
        ),
    ]
