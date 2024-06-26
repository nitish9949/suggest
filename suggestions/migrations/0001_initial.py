# Generated by Django 2.1.7 on 2024-06-08 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=100)),
                ('min_gpa', models.FloatField()),
                ('min_gre_score', models.IntegerField()),
                ('min_toefl_score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gpa', models.FloatField()),
                ('gre_score', models.IntegerField()),
                ('toefl_score', models.IntegerField()),
            ],
        ),
    ]
