# Generated by Django 3.0.8 on 2020-07-30 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_auto_20200730_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='friday',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='monday',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='thursday',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='tuesday',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='wednesday',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
