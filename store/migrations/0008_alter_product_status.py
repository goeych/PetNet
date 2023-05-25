# Generated by Django 4.2.1 on 2023-05-24 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, choices=[('active11', 'active'), ('inactive', 'inactive'), ('cal_progress', 'cal_progress'), ('decommission', 'decommission')], default='active11', max_length=50, null=True),
        ),
    ]