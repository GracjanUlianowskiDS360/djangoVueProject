from django.db import models


class Worker(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    email = models.EmailField()

    def __str__(self):
        return f'{self.name} {self.surname}'
