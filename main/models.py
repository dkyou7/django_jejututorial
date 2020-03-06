from django.db import models

# Create your models here.
class Cafe(models.Model):
    cafeName = models.CharField(max_length=50)
    cafeImg = models.ImageField(blank=True,null=True)
    description = models.TextField()

    def __str__(self):
        return self.cafeName

