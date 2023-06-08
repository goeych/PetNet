# Generated by Django 4.2.1 on 2023-06-08 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0007_calibration_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='calibration',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='attachments/'),
        ),
        migrations.AlterField(
            model_name='calibration',
            name='department_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calibrations', to='equipment.department', verbose_name='Department'),
        ),
        migrations.AlterField(
            model_name='calibration',
            name='equipment_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='calibrations', to='equipment.equipment', verbose_name='Equipment ID'),
        ),
    ]