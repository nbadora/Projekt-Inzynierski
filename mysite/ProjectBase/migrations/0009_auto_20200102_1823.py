# Generated by Django 2.2.7 on 2020-01-02 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectBase', '0008_auto_20191126_1908'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]
