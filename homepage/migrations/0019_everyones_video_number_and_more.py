# Generated by Django 4.2.1 on 2023-08-27 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0018_remove_inner_webinar_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='EVERYONES_VIDEO_NUMBER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tax_Video_Number', models.IntegerField(default=1)),
                ('Long_Term_Care_Video_number', models.IntegerField(default=1)),
                ('Retirement_Video_Number', models.IntegerField(default=1)),
                ('Savings_Video_Number', models.IntegerField(default=1)),
                ('Life_Insurance_Video_Number', models.IntegerField(default=1)),
                ('Asset_Protection_Video_Number', models.IntegerField(default=1)),
                ('Estate_Planning_Video_Number', models.IntegerField(default=1)),
                ('Medicare_Video_Number', models.IntegerField(default=1)),
                ('Other_Video_Number', models.IntegerField(default=1)),
                ('Real_Estate_Investment_Video_Number', models.IntegerField(default=1)),
                ('General_Financial_Planning_Video_Number', models.IntegerField(default=1)),
                ('Company_Structure_Video_Number', models.IntegerField(default=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='verifed_user',
            name='estate_planning_video_number',
        ),
        migrations.RemoveField(
            model_name='verifed_user',
            name='investment_video_number',
        ),
        migrations.RemoveField(
            model_name='verifed_user',
            name='life_insurance_video_number',
        ),
        migrations.RemoveField(
            model_name='verifed_user',
            name='long_term_care_video_number',
        ),
        migrations.RemoveField(
            model_name='verifed_user',
            name='medicare_video_number',
        ),
        migrations.RemoveField(
            model_name='verifed_user',
            name='other_video_number',
        ),
        migrations.RemoveField(
            model_name='verifed_user',
            name='retirement_video_number',
        ),
        migrations.RemoveField(
            model_name='verifed_user',
            name='savings_video_number',
        ),
        migrations.RemoveField(
            model_name='verifed_user',
            name='tax_video_number',
        ),
    ]