from django.db import models

# Create your models here.


DELIVERY_TYPES = (
        ('FD', 'Fast Delivery'),
        ('MD', 'Within 2 to 4 days'),
        ('LD', 'Within a Week'),
)

SHIPMENT_TYPES = (
        ('R', 'Return'), 
        ('F', 'Forward'),
)


class Product(models.Model):
    pick_up_location = models.CharField(max_length=100, help_text="character limit 100")
    destination = models.CharField(max_length=100, help_text="character limit 100")
    length = models.FloatField()
    width = models.FloatField()
    Height = models.FloatField()
    weight = models.FloatField()
    delivery_type = models.CharField(max_length=50, choices=DELIVERY_TYPES)
    shipment_type = models.CharField(max_length=30, choices=SHIPMENT_TYPES)
