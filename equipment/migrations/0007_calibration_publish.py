# Generated by Django 4.2.1 on 2023-06-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0006_equipment_manufacturer_equipment_model_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='calibration',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]
