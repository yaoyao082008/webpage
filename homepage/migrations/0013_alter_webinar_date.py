# Generated by Django 4.2.1 on 2023-07-31 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0012_webinar_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webinar',
            name='date',
            field=models.DateField(),
        ),
    ]
