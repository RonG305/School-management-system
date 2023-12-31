# Generated by Django 4.1.7 on 2023-07-11 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students_api', '0012_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('class_mastering', models.CharField(max_length=50)),
                ('teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students_api.teacher')),
            ],
        ),
    ]
