# Generated by Django 3.1.5 on 2023-07-18 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandidateProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree_level', models.CharField(max_length=100)),
                ('degree_name', models.CharField(max_length=100)),
                ('degree_cgpa', models.DecimalField(decimal_places=2, max_digits=5)),
                ('degree_institution', models.CharField(max_length=100)),
                ('employment_status', models.CharField(max_length=50)),
                ('employment_type', models.CharField(max_length=100)),
                ('areas_of_work', models.CharField(max_length=100)),
                ('total_experience', models.IntegerField()),
                ('target_degree_year', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=50)),
            ],
        ),
    ]