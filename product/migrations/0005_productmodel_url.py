# Generated by Django 4.2.8 on 2024-01-08 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_productmodel_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='url',
            field=models.URLField(null=True),
        ),
    ]