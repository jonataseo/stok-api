# Generated by Django 3.1.1 on 2020-09-19 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0002_sale_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sale',
            name='products',
        ),
    ]