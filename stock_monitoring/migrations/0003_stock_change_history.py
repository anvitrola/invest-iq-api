# Generated by Django 4.1.5 on 2023-10-08 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_monitoring', '0002_remove_stock_actual_price_stock_change_stock_close_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='change_history',
            field=models.TextField(null=True),
        ),
    ]
