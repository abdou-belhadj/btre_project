# Generated by Django 2.1.8 on 2019-06-26 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_auto_20190626_1737'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='style',
            new_name='biens',
        ),
    ]
