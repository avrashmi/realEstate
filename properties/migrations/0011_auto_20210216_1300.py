# Generated by Django 3.1.6 on 2021-02-16 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0010_auto_20210216_1214'),
    ]

    operations = [
        migrations.RenameField(
            model_name='propertycost',
            old_name='property_name',
            new_name='property_type',
        ),
        migrations.RemoveField(
            model_name='propertycost',
            name='name',
        ),
        migrations.RemoveField(
            model_name='propertystatus',
            name='name',
        ),
        migrations.AddField(
            model_name='propertystatus',
            name='property_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='properties.property'),
            preserve_default=False,
        ),
    ]