# Generated by Django 2.2.14 on 2021-05-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_customer', '0003_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='days',
            field=models.DecimalField(decimal_places=2, max_digits=65),
        ),
    ]
