# Generated by Django 2.2.7 on 2020-01-05 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectBase', '0020_auto_20200105_2002'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logo',
            old_name='logo.jpg',
            new_name='image',
        ),
    ]
