# Generated by Django 4.0.1 on 2022-01-15 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriber',
            name='surname',
            field=models.CharField(max_length=80, verbose_name='Surname'),
        ),
    ]
