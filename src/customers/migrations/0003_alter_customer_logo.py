# Generated by Django 3.2.6 on 2021-08-14 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_customer_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='logo',
            field=models.ImageField(default='no_picture.png', upload_to='customers'),
        ),
    ]
