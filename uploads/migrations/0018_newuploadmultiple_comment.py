# Generated by Django 3.1.3 on 2020-11-09 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0017_auto_20201105_1056'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuploadmultiple',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='uploads.imagecomment'),
        ),
    ]
