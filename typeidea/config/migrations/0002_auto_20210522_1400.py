# Generated by Django 2.2.5 on 2021-05-22 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='create_time',
            new_name='created_time',
        ),
    ]
