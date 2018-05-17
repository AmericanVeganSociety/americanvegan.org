# Generated by Django 2.0.5 on 2018-05-17 16:31

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpeakerIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SpeakerPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('name', models.CharField(blank=True, help_text='Name and titles of speaker, ex. Maria Sand, MSW, LSC, FBI', max_length=100)),
                ('state', models.CharField(blank=True, help_text='ex. PA', max_length=100)),
                ('talks', wagtail.core.fields.RichTextField(blank=True, help_text='A sample of talks the speaker may provide, ex. Eating for Cancer Survival')),
                ('website', models.URLField(blank=True, help_text="The speaker's personal or professional website")),
                ('email', models.EmailField(blank=True, help_text='An email by which the speaker may be contacted', max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='A phone number by which the speaker may be contacted', max_length=128)),
                ('bio', wagtail.core.fields.RichTextField(blank=True, help_text='describe the event')),
                ('headshot', models.ForeignKey(blank=True, help_text='A nice headshot of the speaker', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]