# Generated by Django 2.2.14 on 2021-05-18 04:48

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_owner', '0006_remove_houses_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='houseowner',
            name='password',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(limit_value=6)]),
        ),
    ]
