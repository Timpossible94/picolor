from django.db import models

class Bild(models.Model):
    name = models.CharField(max_length=200, null=True)
    beschreibung = models.TextField(null=True, blank=True)
    bild = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name