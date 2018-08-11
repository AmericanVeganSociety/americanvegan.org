# Generated by Django 2.0.5 on 2018-08-11 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('portals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portalpage',
            name='listing_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
