# Generated by Django 2.2.6 on 2019-11-12 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flex', '0005_flexpage_banner_i'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flexpage',
            old_name='banner_i',
            new_name='flex_image',
        ),
    ]
