# Generated by Django 4.1.7 on 2023-06-16 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='student_number',
        ),
    ]
