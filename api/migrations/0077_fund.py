# Generated by Django 3.2.16 on 2023-12-09 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0076_rename_fund_manager_id_fundwithdraw_fund_manager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit_amount', models.BigIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('fund_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.fundmanager')),
            ],
        ),
    ]
