from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    gpa = models.FloatField()
    gre_score = models.IntegerField()
    toefl_score = models.IntegerField()
    duolingo_score = models.IntegerField()
    ielts_score = models.FloatField()

class College(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    min_gpa = models.FloatField()
    min_gre_score = models.IntegerField()
    min_toefl_score = models.IntegerField()
    min_duolingo_score = models.IntegerField()
    min_ielts_score = models.FloatField()
