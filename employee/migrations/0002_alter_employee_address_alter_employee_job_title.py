# Generated by Django 5.0.2 on 2024-02-15 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='employee',
            name='job_title',
            field=models.TextField(max_length=500),
        ),
    ]
