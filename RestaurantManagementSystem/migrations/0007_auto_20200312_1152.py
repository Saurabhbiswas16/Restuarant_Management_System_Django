# Generated by Django 3.0.2 on 2020-03-12 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantManagementSystem', '0006_auto_20200312_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_information',
            name='customer_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]