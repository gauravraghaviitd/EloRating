from django.db import models
from elo.managers import modelManager

# Create your models here.

class model(models.Model):
    score = models.IntegerField()
    image = models.CharField(max_length=100)
    is_valid = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    exposure = models.IntegerField(default=0)

    objects = modelManager()

    class Meta:
        db_table = 'model'

    def __str__(self):
        return "score: " + self.score + " | image: " + self.image
