# Generated by Django 4.2.11 on 2024-04-25 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0008_alter_employer_image_alter_viauser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='appliedjobs',
            name='email',
            field=models.CharField(default='Unknown', max_length=255),
            preserve_default=False,
        ),
    ]