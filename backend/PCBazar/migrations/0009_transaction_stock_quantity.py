# Generated by Django 5.1.1 on 2024-10-29 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PCBazar', '0008_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='stock_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
