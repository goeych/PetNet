# Generated by Django 4.2.1 on 2023-06-16 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipment', '0011_equipment_due_cal_equipment_last_cal'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='caltype',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
