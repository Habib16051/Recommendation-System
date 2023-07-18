# Generated by Django 3.1.5 on 2022-08-18 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('subject', models.CharField(max_length=350, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
            ],
        ),
    ]