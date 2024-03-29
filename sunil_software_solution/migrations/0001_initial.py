# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-07-27 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30)),
                ('start_date', models.DateField(max_length=30)),
                ('course_fee', models.IntegerField()),
                ('faculty_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FeedbackData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('rating', models.IntegerField()),
                ('date', models.DateField(max_length=50)),
                ('feedback', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student_Enquiry_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('mobile_no', models.BigIntegerField()),
                ('qualification', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
            ],
        ),
    ]
