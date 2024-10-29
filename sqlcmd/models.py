from django.db import models


# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class UserModels(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    telephone = models.CharField(max_length=11)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
