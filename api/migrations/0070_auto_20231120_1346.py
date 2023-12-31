# Generated by Django 3.2.16 on 2023-11-20 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0069_rename_class_id_investmentperformance_investment_option'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiskAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('cash', models.IntegerField(default=0)),
                ('credit', models.IntegerField(default=0)),
                ('venture', models.IntegerField(default=0)),
                ('absolute_return', models.IntegerField(default=0)),
                ('score_range', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='riskprofile',
            name='risk_analysis',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.riskanalysis'),
        ),
    ]
