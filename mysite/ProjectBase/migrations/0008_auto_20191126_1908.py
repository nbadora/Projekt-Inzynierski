# Generated by Django 2.2.7 on 2019-11-26 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectBase', '0007_auto_20191126_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=200, verbose_name='Product Name'),
        ),
    ]
