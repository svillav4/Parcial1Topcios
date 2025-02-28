from django.db import models

class Flight(models.Model):
    TYPE_CHOICES = [
        ('Nacional', 'Nacional'),
        ('Internacional', 'Internacional'),
    ]
    name = models.CharField(max_length=255)
    typee = models.CharField(max_length=13, choices=TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)