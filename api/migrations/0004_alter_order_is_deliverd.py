# Generated by Django 5.0.1 on 2024-02-09 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_deliverd',
            field=models.BooleanField(default=0),
        ),
    ]
