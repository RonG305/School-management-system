# Generated by Django 4.1.7 on 2023-07-11 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students_api', '0014_classteacher_stream_alter_student_stream'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolPerformance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
                ('score', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
        ),
        migrations.AlterField(
            model_name='classteacher',
            name='class_mastering',
            field=models.CharField(choices=[('FORM 1', 'Form 1'), ('FORM 2', 'Form 2'), ('FORM 3', 'Form 3'), ('FORM 4', 'Form 4')], max_length=50),
        ),
    ]
