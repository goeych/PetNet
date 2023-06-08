# Generated by Django 4.2.1 on 2023-06-07 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0005_remove_calibration_department_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='manufacturer',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='model_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='equipment',
            name='serial_no',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
