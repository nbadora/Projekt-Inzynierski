# Generated by Django 2.2.7 on 2020-01-05 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectBase', '0014_auto_20200104_2202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='gallery', verbose_name='Picture')),
            ],
        ),
    ]
