# Generated by Django 3.0.3 on 2020-05-16 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrdashapp', '0009_auto_20200514_0814'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='location',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
