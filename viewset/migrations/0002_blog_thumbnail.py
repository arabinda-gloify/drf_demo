# Generated by Django 3.0.6 on 2020-05-05 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewset', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]