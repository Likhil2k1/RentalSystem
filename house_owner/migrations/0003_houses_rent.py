# Generated by Django 2.2.14 on 2021-05-14 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_owner', '0002_houses'),
    ]

    operations = [
        migrations.AddField(
            model_name='houses',
            name='rent',
            field=models.DecimalField(decimal_places=2, default=9000, max_digits=65),
        ),
    ]
