# Generated by Django 2.1.8 on 2019-06-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_listing_placeparking'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='abri',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='listing',
            name='cellier',
            field=models.BooleanField(default=False),
        ),
    ]