# Generated by Django 3.2.8 on 2021-10-26 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_post', '0009_alter_userimage_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userimage',
            name='user_image',
            field=models.FileField(null=True, upload_to='images/uploads'),
        ),
    ]
