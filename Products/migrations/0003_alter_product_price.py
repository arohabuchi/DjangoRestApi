# Generated by Django 4.2.2 on 2023-07-23 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0002_alter_product_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=3, default=99.0, max_digits=10),
        ),
    ]
