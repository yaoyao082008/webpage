# Generated by Django 4.2.5 on 2025-01-28 01:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0020_rename_everyones_video_number_everyone_video_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='verifed_user',
            options={'permissions': (('licensed_member', 'Licensed Member'),)},
        ),
    ]
