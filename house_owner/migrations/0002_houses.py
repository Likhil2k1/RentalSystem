# Generated by Django 2.2.14 on 2021-05-12 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house_owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Houses',
            fields=[
                ('owner_name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('default', 'Select Type'), ('Apartment Flat', 'APARTMENT FLAT'), ('Bungalow', 'BUNGALOW'), ('Villa', 'VILLA'), ('Duplex', 'DUPLEX'), ('Others', 'OTHERS')], default='default', max_length=100)),
                ('bed_rooms', models.CharField(choices=[('default', 'No.of Bedrooms'), ('1', '1'), ('2', '2'), ('3', '3')], default='default', max_length=100)),
                ('category', models.CharField(choices=[('default', 'Select Category'), ('For Sale', 'For Sale'), ('For Rent', 'For Rent')], default='default', max_length=100)),
                ('image1', models.ImageField(upload_to='images/')),
                ('image2', models.ImageField(upload_to='images/')),
                ('image3', models.ImageField(upload_to='images/')),
                ('area', models.IntegerField()),
                ('doorno', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'owner_houses',
            },
        ),
    ]
