# Generated by Django 4.2.8 on 2024-01-08 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_productmodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='file',
            field=models.FileField(null=True, upload_to='files/'),
        ),
    ]
