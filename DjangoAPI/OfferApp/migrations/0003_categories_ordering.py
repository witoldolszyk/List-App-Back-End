# Generated by Django 3.2.10 on 2022-01-08 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OfferApp', '0002_auto_20220108_2233'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='Ordering',
            field=models.CharField(default='SOME STRING', max_length=100),
        ),
    ]
