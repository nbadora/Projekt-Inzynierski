# Generated by Django 2.2.7 on 2020-01-07 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectBase', '0025_auto_20200107_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='new',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
