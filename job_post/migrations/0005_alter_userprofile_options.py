# Generated by Django 3.2.8 on 2021-10-26 03:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_post', '0004_auto_20211024_2219'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['last_name']},
        ),
    ]