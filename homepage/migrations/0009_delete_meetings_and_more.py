# Generated by Django 4.2.1 on 2023-07-20 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_rename_video_number_verifed_user_estate_planning_video_number_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='meetings',
        ),
        migrations.AlterField(
            model_name='verifed_user',
            name='estate_planning_video_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='verifed_user',
            name='investment_video_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='verifed_user',
            name='life_insurance_video_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='verifed_user',
            name='long_term_care_video_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='verifed_user',
            name='medicare_video_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='verifed_user',
            name='retirement_video_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='verifed_user',
            name='savings_video_number',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='verifed_user',
            name='tax_video_number',
            field=models.IntegerField(default=1),
        ),
    ]