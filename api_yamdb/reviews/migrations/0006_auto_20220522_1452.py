# Generated by Django 2.2.16 on 2022-05-22 11:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20220522_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='score',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Оценка'),
        ),
    ]