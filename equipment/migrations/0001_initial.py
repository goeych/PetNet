# Generated by Django 4.2.1 on 2023-06-07 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calibration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_id', models.CharField(blank=True, max_length=50, null=True)),
                ('last_cal', models.DateField()),
                ('due_cal', models.DateField()),
                ('complete', models.BooleanField(default=False)),
                ('remark', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('due_cal',),
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment_id', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.IntegerField(blank=True, null=True)),
                ('ref_standard', models.CharField(blank=True, max_length=200, null=True)),
                ('nist_no', models.CharField(blank=True, max_length=50, null=True)),
                ('serial_no', models.CharField(blank=True, max_length=50, null=True)),
                ('asset_no', models.CharField(blank=True, max_length=50, null=True)),
                ('model_no', models.CharField(blank=True, max_length=50, null=True)),
                ('caltype', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('unit_of_meas', models.CharField(blank=True, max_length=50, null=True)),
                ('drawing_no', models.CharField(blank=True, max_length=50, null=True)),
                ('drawing_date', models.CharField(blank=True, max_length=50, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('storage_location', models.CharField(blank=True, max_length=50, null=True)),
                ('current_location', models.CharField(blank=True, max_length=50, null=True)),
                ('service_date', models.DateTimeField(blank=True, null=True)),
                ('retirement_date', models.DateTimeField(blank=True, null=True)),
                ('supplier_code', models.CharField(blank=True, max_length=50, null=True)),
                ('cost', models.FloatField(blank=True, null=True)),
                ('purchase_date', models.DateTimeField(blank=True, null=True)),
                ('user_defined', models.TextField(blank=True, null=True)),
                ('manufacturer', models.CharField(blank=True, max_length=50, null=True)),
                ('owner', models.CharField(blank=True, max_length=50, null=True)),
                ('vendor_contact', models.CharField(blank=True, max_length=50, null=True)),
                ('cal_item', models.CharField(blank=True, max_length=50, null=True)),
                ('cal_type', models.CharField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.department')),
            ],
        ),
        migrations.CreateModel(
            name='WeeklyMonitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipment.equipment')),
            ],
        ),
    ]
