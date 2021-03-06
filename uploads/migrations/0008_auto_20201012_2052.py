# Generated by Django 2.2 on 2020-10-12 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0007_auto_20201012_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagegalery',
            name='image_inst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_list', to='uploads.NewUploadMultiple'),
        ),
        migrations.AlterField(
            model_name='likeimage',
            name='image_inst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_list', to='uploads.NewUploadMultiple'),
        ),
        migrations.AlterField(
            model_name='newuploadmultiple',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='ImageComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=50, null=True)),
                ('user', models.CharField(max_length=10, null=True)),
                ('image_inst', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_list', to='uploads.NewUploadMultiple')),
            ],
        ),
    ]
