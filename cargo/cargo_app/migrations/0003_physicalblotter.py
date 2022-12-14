# Generated by Django 4.1.2 on 2022-10-29 19:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cargo_app', '0002_pricingmethodemodel_strategymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhysicalBlotter',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('Date', models.DateField(default=datetime.datetime.now)),
                ('Trader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargo_app.tradermodel')),
            ],
        ),
    ]
