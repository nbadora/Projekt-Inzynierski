# Generated by Django 2.2.7 on 2020-01-07 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectBase', '0022_delete_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='desc',
            field=models.CharField(default='0000000', max_length=1000, verbose_name='Product Description'),
        ),
    ]
