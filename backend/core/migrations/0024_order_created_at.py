# Generated by Django 5.0.7 on 2024-08-18 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_remove_order_active_remove_order_cart_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
