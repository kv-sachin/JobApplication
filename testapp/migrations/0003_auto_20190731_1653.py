# Generated by Django 2.2.3 on 2019-07-31 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_noidajobs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noidajobs',
            old_name='compnay',
            new_name='company',
        ),
    ]
