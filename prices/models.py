from django.db import models


class Price(models.Model):
    Category = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.Category