from django.db import models
from django.utils import timezone

# Create your models here.

class Artifact(models.Model):
    name = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='images')
    origin = models.CharField(max_length=200, default='')
    age = models.CharField(max_length=200, default='')
    description = models.TextField()
    crafting = models.TextField()
    trajectory = models.TextField()
    
    expert_value = models.DecimalField(max_digits=9, decimal_places=2)
    current_bidding_price = models.DecimalField(max_digits=9, decimal_places=2)
    buy_now_price = models.DecimalField(max_digits=9, decimal_places=2)
    
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    bidding_time = models.IntegerField(default=0)
    
    on_bidding = models.BooleanField(blank=False, default=True)

    def __str__(self):
        return self.name