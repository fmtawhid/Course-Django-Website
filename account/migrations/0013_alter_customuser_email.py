# Generated by Django 4.2.7 on 2024-06-27 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_alter_customuser_bio_alter_customuser_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
