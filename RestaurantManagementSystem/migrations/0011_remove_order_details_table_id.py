# Generated by Django 3.0.2 on 2020-03-15 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantManagementSystem', '0010_auto_20200315_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_details',
            name='table_id',
        ),
    ]
