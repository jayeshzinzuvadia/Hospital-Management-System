# Generated by Django 3.0.2 on 2020-03-08 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('email_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=7)),
                ('img_url', models.CharField(max_length=50)),
                ('typeofdoctor', models.CharField(max_length=20)),
                ('degree', models.CharField(max_length=30)),
                ('hospital_address', models.CharField(max_length=50)),
                ('phoneno', models.IntegerField()),
                ('birthdate', models.DateField(verbose_name='date of birth')),
            ],
        ),
    ]
