# Generated by Django 3.2.6 on 2021-08-14 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='logo',
            field=models.ImageField(default='no_picture.jpeg', upload_to='customers'),
        ),
    ]
