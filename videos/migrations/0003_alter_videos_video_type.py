# Generated by Django 4.1.8 on 2023-05-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_alter_videos_video_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='video_type',
            field=models.TextField(choices=[('tax', 'Taxes'), ('saving', 'College/University Savings'), ('retirement', 'Retirement Plans'), ('life_insurance', 'Life Insurance'), ('investment', 'Investment'), ('estate_planning', 'Estate Planning'), ('long_term_care', 'Long Term Care'), ('medicare', 'Medicare')], default='tax'),
        ),
    ]
