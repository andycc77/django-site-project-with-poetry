from django.db import models


class TB_1(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
