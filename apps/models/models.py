from django.db import models

class RoosterData(models.Model):
    clt = models.CharField(max_length=100)
    date = models.DateField()
    meta_value = models.TextField()

    def __str__(self):
        return self.clt
