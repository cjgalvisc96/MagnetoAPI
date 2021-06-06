from django.db import models


class Stats(models.Model):
    count_mutant_dna = models.IntegerField()
    count_human_dna = models.IntegerField()
    ratio = models.FloatField()
