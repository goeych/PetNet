# Generated by Django 4.2.1 on 2023-06-07 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0004_calibration_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calibration',
            name='department',
        ),
        migrations.RemoveField(
            model_name='calibration',
            name='equipment_id',
        ),
    ]
