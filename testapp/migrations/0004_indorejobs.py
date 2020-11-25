# Generated by Django 3.1.3 on 2020-11-25 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_auto_20190731_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='indorejobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('eligibility', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.IntegerField()),
            ],
        ),
    ]