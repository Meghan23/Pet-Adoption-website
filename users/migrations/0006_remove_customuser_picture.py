# Generated by Django 2.1 on 2018-08-23 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20180823_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='picture',
        ),
    ]