# Generated by Django 2.1 on 2018-08-23 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20180823_2020'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='photo',
        ),
    ]