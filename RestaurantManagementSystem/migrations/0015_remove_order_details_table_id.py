# Generated by Django 3.0.2 on 2020-03-17 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantManagementSystem', '0014_order_details_table_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_details',
            name='table_id',
        ),
    ]
