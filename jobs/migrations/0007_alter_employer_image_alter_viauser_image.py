# Generated by Django 4.2.11 on 2024-04-25 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_alter_appliedjobs_marksheet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='image',
            field=models.ImageField(default='Unknown', upload_to='media/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='viauser',
            name='image',
            field=models.ImageField(default='Unknown', upload_to='media/'),
            preserve_default=False,
        ),
    ]
