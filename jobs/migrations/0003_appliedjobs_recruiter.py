# Generated by Django 4.2.11 on 2024-04-24 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_alter_appliedjobs_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliedjobs',
            name='recruiter',
            field=models.CharField(default='Unknown', max_length=255),
            preserve_default=False,
        ),
    ]