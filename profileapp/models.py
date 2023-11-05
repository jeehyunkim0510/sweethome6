from django.db import models

# Create your models here.
from django.db import models



class Family(models.Model):
    family_name = models.CharField(max_length=20, null=False)
