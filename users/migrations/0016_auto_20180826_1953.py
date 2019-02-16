# Generated by Django 2.1 on 2018-08-26 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20180826_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='city',
            field=models.CharField(choices=[('Kanpur', 'Kanpur'), ('Visakhapatnam', 'Visakhapatnam'), ('Surat', 'Surat'), ('Chennai', 'Chennai'), ('Hyderabad', 'Hyderabad'), ('Pune', 'Pune'), ('Bangalore', 'Bangalore'), ('Kolkata', 'Kolkata'), ('Mumbai', 'Mumbai'), ('Delhi', 'Delhi')], max_length=50),
        ),
        migrations.AlterField(
            model_name='pet',
            name='color',
            field=models.CharField(choices=[('Black', 'Black'), ('Brindle', 'Brindle'), ('Brown/Chocolate', 'Brown/Chocolate'), ('Gray/Blue/Silver/Salt & Pepper', 'Gray/Blue/Silver/Salt & Pepper'), ('Merle', 'Merle'), ('Red/Golden/Orange/Chestnut', 'Red/Golden/Orange/Chestnut'), ('Silver & Tan (Yorkie colors)', 'Silver & Tan (Yorkie colors)'), ('Tan/Yellow/Fawn', 'Tan/Yellow/Fawn'), ('Tricolor (Tan/Brown & Black & White', 'Tricolor (Tan/Brown & Black & White'), ('White', 'White')], max_length=15),
        ),
    ]
