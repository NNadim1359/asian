# Generated by Django 2.2.6 on 2019-11-12 06:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactpage',
            name='contact_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
