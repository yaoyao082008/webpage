# Generated by Django 4.2.5 on 2024-01-08 22:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='asset_protection_video',
            fields=[
                ('my_order', models.PositiveIntegerField(default=0)),
                ('link', models.CharField(max_length=1000)),
                ('password', models.CharField(default='N/A', max_length=40)),
                ('title', models.CharField(default='Title', max_length=500)),
                ('author', models.CharField(default='Anonymous', max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
        migrations.CreateModel(
            name='college_university_savings_video',
            fields=[
                ('my_order', models.PositiveIntegerField(default=0)),
                ('link', models.CharField(max_length=1000)),
                ('password', models.CharField(default='N/A', max_length=40)),
                ('title', models.CharField(default='Title', max_length=500)),
                ('author', models.CharField(default='Anonymous', max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
        migrations.CreateModel(
            name='Company_Structure_Video',
            fields=[
                ('my_order', models.PositiveIntegerField(default=0)),
                ('link', models.CharField(max_length=1000)),
                ('password', models.CharField(default='N/A', max_length=40)),
                ('title', models.CharField(default='Title', max_length=500)),
                ('author', models.CharField(default='Anonymous', max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
        migrations.CreateModel(
            name='estate_planning_video',
            fields=[
                ('my_order', models.PositiveIntegerField(default=0)),
                ('link', models.CharField(max_length=1000)),
                ('password', models.CharField(default='N/A', max_length=40)),
                ('title', models.CharField(default='Title', max_length=500)),
                ('author', models.CharField(default='Anonymous', max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
        migrations.CreateModel(
            name='exam_video',
            fields=[
                ('my_order', models.PositiveIntegerField(default=0)),
                ('link', models.CharField(max_length=1000)),
                ('password', models.CharField(default='N/A', max_length=40)),
                ('title', models.CharField(default='Title', max_length=500)),
                ('author', models.CharField(default='Anonymous', max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
        migrations.CreateModel(
            name='General_Financial_Planning_Video',
            fields=[
                ('my_order', models.PositiveIntegerField(default=0)),
                ('link', models.CharField(max_length=1000)),
                ('password', models.CharField(default='N/A', max_length=40)),
                ('title', models.CharField(default='Title', max_length=500)),
                ('author', models.CharField(default='Anonymous', max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
        migrations.CreateModel(
            name='life_insurance_video',
            fields=[
                ('my_order', models.PositiveIntegerField(default=0)),
                ('link', models.CharField(max_length=1000)),
                ('password', models.CharField(default='N/A', max_length=40)),
                ('title', models.CharField(default='Title', max_length=500)),
                ('author', models.CharField(default='Anonymous', max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
        migrations.CreateModel(
            name='long_term_care_video',
            fields=[
                ('my_order', models.PositiveIntegerField(default=0)),
                ('link', models.CharField(max_length=1000)),
                ('password', models.CharField(default='N/A', max_length=40)),
                ('title', models.CharField(default='Title', max_length=500)),
                ('author', models.CharField(default='Anonymous', max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
        migrations.CreateModel(
            name='medicare_video',
            fields=[
                ('my_order', models.PositiveIntegerField(default=0)),
                ('link', models.CharField(max_length=1000)),
                ('password', models.CharField(default='N/A', max_length=40)),
                ('title', models.CharField(default='Title', max_length=500)),
                ('author', models.CharField(default='Anonymous', max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
        migrations.CreateModel(
            name='other_video',
            fields=[
                ('my_order', models.PositiveIntegerField(default=0)),
                ('link', models.CharField(max_length=1000)),
                ('password', models.CharField(default='N/A', max_length=40)),
                ('title', models.CharField(default='Title', max_length=500)),
                ('author', models.CharField(default='Anonymous', max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
        migrations.CreateModel(
            name='Real_Estate_Investment_Video',
            fields=[
                ('my_order', models.PositiveIntegerField(default=0)),
                ('link', models.CharField(max_length=1000)),
                ('password', models.CharField(default='N/A', max_length=40)),
                ('title', models.CharField(default='Title', max_length=500)),
                ('author', models.CharField(default='Anonymous', max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
        migrations.CreateModel(
            name='retirement_video',
            fields=[
                ('my_order', models.PositiveIntegerField(default=0)),
                ('link', models.CharField(max_length=1000)),
                ('password', models.CharField(default='N/A', max_length=40)),
                ('title', models.CharField(default='Title', max_length=500)),
                ('author', models.CharField(default='Anonymous', max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
        migrations.CreateModel(
            name='tax_video',
            fields=[
                ('my_order', models.PositiveIntegerField(default=0)),
                ('link', models.CharField(max_length=1000)),
                ('password', models.CharField(default='N/A', max_length=40)),
                ('title', models.CharField(default='Title', max_length=500)),
                ('author', models.CharField(default='Anonymous', max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['my_order'],
            },
        ),
    ]
