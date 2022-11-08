# Generated by Django 4.1.2 on 2022-10-29 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo_app', '0003_physicalblotter'),
    ]

    operations = [
        migrations.AddField(
            model_name='physicalblotter',
            name='Book',
            field=models.CharField(choices=[('Book1', 'Book1'), ('Book2', 'Book2')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='physicalblotter',
            name='Counter_Party',
            field=models.CharField(choices=[('X', 'X'), ('Y', 'Y'), ('Z', 'Z')], default='X', max_length=120),
        ),
    ]