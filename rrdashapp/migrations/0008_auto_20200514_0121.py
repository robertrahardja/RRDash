# Generated by Django 3.0.3 on 2020-05-14 01:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rrdashapp', '0007_auto_20200513_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rrdashapp.Restaurant'),
        ),
    ]
