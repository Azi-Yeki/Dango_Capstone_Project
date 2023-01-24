from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=140)
    details = models.TextField()
    date = models.DateTimeField

    def __str__(self):
        return self.name


