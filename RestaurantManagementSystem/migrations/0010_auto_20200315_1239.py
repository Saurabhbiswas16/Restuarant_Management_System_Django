# Generated by Django 3.0.2 on 2020-03-15 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantManagementSystem', '0009_auto_20200313_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order_details',
            name='emp_id',
        ),
        migrations.AddField(
            model_name='order_details',
            name='amount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order_details',
            name='fooditem_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='RestaurantManagementSystem.Fooditems_Details'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order_details',
            name='fooditem_price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order_details',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order_details',
            name='order_id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Order_Items',
        ),
    ]