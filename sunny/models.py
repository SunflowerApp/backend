from django.db import models

# Create your models here.
class Test(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    votes2 = models.IntegerField(default=0)