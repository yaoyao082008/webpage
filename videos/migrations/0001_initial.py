# Generated by Django 4.2.1 on 2023-05-12 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1000)),
                ('password', models.CharField(max_length=40)),
                ('video_type', models.TextField(choices=[('tax', 'Taxes'), ('insurance', 'life_insurance')], default='tax')),
            ],
        ),
    ]
