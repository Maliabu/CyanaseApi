# Generated by Django 3.2.16 on 2023-11-13 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0068_auto_20231113_1557'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investmentperformance',
            old_name='class_id',
            new_name='investment_option',
        ),
    ]