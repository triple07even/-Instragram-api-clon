# Generated by Django 3.1.3 on 2020-12-09 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0049_auto_20201209_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsoreduploadmultiple',
            name='detail',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
