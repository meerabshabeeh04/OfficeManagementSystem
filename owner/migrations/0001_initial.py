# Generated by Django 5.0.2 on 2024-02-08 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emaill', models.CharField(max_length=500)),
                ('passwordd', models.CharField(max_length=500)),
            ],
        ),
    ]
