# Generated by Django 4.0.1 on 2022-01-15 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='deadline',
            field=models.DateField(),
        ),
    ]
