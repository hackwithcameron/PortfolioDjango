# Generated by Django 3.0.7 on 2020-12-23 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0004_auto_20201223_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email_Address',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='first_Name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='last_Name',
            field=models.CharField(max_length=30),
        ),
    ]
