from django.db import models

class TempLog(models.Model):
    temp = models.CharField(max_length=10)
    time = models.DateTimeField(auto_now_add=True, auto_now=False, blank=False)

