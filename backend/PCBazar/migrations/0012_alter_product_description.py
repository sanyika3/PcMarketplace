# Generated by Django 5.1.1 on 2024-11-01 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PCBazar', '0011_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=3000),
        ),
    ]
