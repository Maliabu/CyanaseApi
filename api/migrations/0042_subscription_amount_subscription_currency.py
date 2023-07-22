# Generated by Django 4.1.3 on 2023-07-21 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0041_remove_subscription_transaction_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='amount',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='subscription',
            name='currency',
            field=models.CharField(default='UGX', max_length=200),
        ),
    ]