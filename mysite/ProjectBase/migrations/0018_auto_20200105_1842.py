# Generated by Django 2.2.7 on 2020-01-05 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectBase', '0017_auto_20200105_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logo',
            name='image',
            field=models.ImageField(blank=True, upload_to='gallery', verbose_name='Picture'),
        ),
    ]
