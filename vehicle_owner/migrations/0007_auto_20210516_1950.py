# Generated by Django 2.2.14 on 2021-05-16 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_owner', '0006_vehicles_is_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='image1',
            field=models.ImageField(upload_to='static/images/vehicles/'),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='image2',
            field=models.ImageField(upload_to='static/images/vehicles/'),
        ),
        migrations.AlterField(
            model_name='vehicles',
            name='image3',
            field=models.ImageField(upload_to='static/images/vehicles/'),
        ),
    ]