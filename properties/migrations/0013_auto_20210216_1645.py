# Generated by Django 3.1.6 on 2021-02-16 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0012_auto_20210216_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertycost',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]