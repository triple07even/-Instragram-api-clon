# Generated by Django 3.1.3 on 2020-11-25 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_auto_20201123_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='sex',
            field=models.CharField(blank=True, choices=[('female', 'Female'), ('male', 'Male')], max_length=6, null=True),
        ),
    ]
