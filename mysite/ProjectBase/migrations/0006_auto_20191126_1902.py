# Generated by Django 2.2.7 on 2019-11-26 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectBase', '0005_auto_20191126_1901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='product',
            name='Product Name',
            field=models.CharField(default='gowno', max_length=200, primary_key=True, serialize=False),
        ),
    ]