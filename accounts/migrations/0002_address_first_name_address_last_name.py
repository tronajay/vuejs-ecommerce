# Generated by Django 4.0.4 on 2022-05-29 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='last_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
