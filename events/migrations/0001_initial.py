# Generated by Django 2.0.5 on 2018-05-16 16:58

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('address_name', models.CharField(blank=True, max_length=100)),
                ('address_street', models.CharField(blank=True, max_length=100)),
                ('address_city', models.CharField(blank=True, max_length=100)),
                ('address_state', models.CharField(blank=True, max_length=100)),
                ('address_zip', models.CharField(blank=True, max_length=100)),
                ('description', wagtail.core.fields.RichTextField(blank=True)),
                ('type', models.CharField(choices=[('AVS', 'AVS'), ('Other', 'Other')], max_length=100)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
