# Generated by Django 4.2.1 on 2023-06-07 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0003_calibration_department_fk_calibration_equipment_fk'),
    ]

    operations = [
        migrations.AddField(
            model_name='calibration',
            name='department',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]