# Generated by Django 3.2.8 on 2021-10-06 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_product_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='img',
        ),
    ]
