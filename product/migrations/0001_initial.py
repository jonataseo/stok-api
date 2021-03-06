# Generated by Django 3.1.1 on 2020-09-16 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('buy_value', models.DecimalField(decimal_places=2, max_digits=8)),
                ('sell_value', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
