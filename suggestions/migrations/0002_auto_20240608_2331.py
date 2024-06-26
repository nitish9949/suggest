# Generated by Django 2.1.7 on 2024-06-08 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suggestions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='min_duolingo_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='college',
            name='min_ielts_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='duolingo_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='ielts_score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
