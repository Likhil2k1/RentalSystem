# Generated by Django 2.2.14 on 2021-05-16 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_owner', '0004_auto_20210516_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='houses',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
