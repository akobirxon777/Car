# Generated by Django 5.0.6 on 2024-07-05 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0004_alter_car_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='like',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
