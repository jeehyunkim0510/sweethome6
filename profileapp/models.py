from django.db import models

# Create your models here.
from django.db import models



from django.contrib.auth.models import User

class Family(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='family', unique=True)
    family_name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.family_name