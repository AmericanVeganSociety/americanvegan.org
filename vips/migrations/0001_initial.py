# Generated by Django 2.0.5 on 2018-05-17 16:31

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='VIPPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='VIPs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='What is the name of the VIP?', max_length=100)),
                ('address_name', models.CharField(blank=True, help_text='Ex. Ithaca College', max_length=100)),
                ('address_street', models.CharField(blank=True, help_text='ex. 123 E South St.', max_length=100)),
                ('address_city', models.CharField(blank=True, help_text='ex. Philadelphia', max_length=100)),
                ('address_state', models.CharField(blank=True, help_text='ex. PA', max_length=100)),
                ('address_zip', models.CharField(blank=True, help_text='ex. 19140', max_length=100)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='ex. 234-567-9895', max_length=100)),
                ('email', models.CharField(blank=True, help_text='ex. jane@smith.edu', max_length=100)),
                ('details', wagtail.core.fields.RichTextField(blank=True, help_text='Any details you would like to share about this person?')),
            ],
        ),
    ]