# Generated by Django 3.0.2 on 2020-03-12 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantManagementSystem', '0007_auto_20200312_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table_master',
            name='customer_id',
        ),
        migrations.AlterField(
            model_name='table_master',
            name='table_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
