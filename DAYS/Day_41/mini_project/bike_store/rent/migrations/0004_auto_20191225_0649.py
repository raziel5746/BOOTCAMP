# Generated by Django 3.0.1 on 2019-12-25 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_auto_20191225_0647'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rental',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='rental',
            old_name='vehicle_id',
            new_name='vehicle',
        ),
    ]
