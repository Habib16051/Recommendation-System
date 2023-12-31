# Generated by Django 3.1.5 on 2023-07-12 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appwebsite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(max_length=350),
        ),
    ]
