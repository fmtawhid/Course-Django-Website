# Generated by Django 4.2.7 on 2024-06-23 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_cartmodel_cartitemmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitemmodel',
            old_name='product',
            new_name='course',
        ),
        migrations.RemoveField(
            model_name='cartitemmodel',
            name='quantity',
        ),
    ]
