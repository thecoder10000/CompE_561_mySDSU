# Generated by Django 4.1.3 on 2022-11-28 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redID', models.CharField(max_length=100, verbose_name='Student RedID')),
                ('email', models.EmailField(max_length=254, verbose_name='Student Email')),
                ('Name', models.CharField(max_length=100, verbose_name='Student Name')),
                ('Major', models.CharField(max_length=100, verbose_name='Student Major')),
            ],
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseNumber', models.CharField(max_length=100, verbose_name='Course Number')),
                ('courseName', models.CharField(max_length=100, verbose_name='Course Name')),
                ('units', models.CharField(max_length=100, verbose_name='Units')),
                ('grade', models.CharField(max_length=100, verbose_name='Grade Recieved')),
                ('gpa', models.CharField(max_length=100, verbose_name='GPA')),
                ('semester', models.CharField(max_length=100, verbose_name='Semester')),
                ('students_took_class', models.ManyToManyField(blank=True, to='members.students')),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseNumber', models.CharField(max_length=100, verbose_name='Course Number')),
                ('courseName', models.CharField(max_length=100, verbose_name='Course Name')),
                ('units', models.CharField(max_length=100, verbose_name='Units')),
                ('dayAndTime', models.CharField(max_length=100, verbose_name='Day / Time')),
                ('location', models.CharField(max_length=100, verbose_name='Location')),
                ('semester', models.CharField(max_length=100, verbose_name='Semester')),
                ('students_in_class', models.ManyToManyField(blank=True, to='members.students')),
            ],
        ),
    ]
