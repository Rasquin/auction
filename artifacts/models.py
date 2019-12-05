from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from django.utils import timezone

# Create your models here.

class Artifact(models.Model):
    name = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='images')
    origin = models.CharField(max_length=200, default='')
    year = models.IntegerField(default=2020, validators=[MinValueValidator(-2000), MaxValueValidator(2020)])
    description = models.TextField()
    crafting = models.TextField()
    trajectory = models.TextField()
    by_user = models.IntegerField(default=1)
    
    expert_value = models.DecimalField(validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('9999999.99'))], max_digits=9, decimal_places=2)
    minimun_bidding_price = models.DecimalField(validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('9999999.99'))], max_digits=9, decimal_places=2)
    current_bidding_price = models.DecimalField(validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('9999999.99'))], max_digits=9, decimal_places=2)
    buy_now_price = models.DecimalField(validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('20000000.00'))], max_digits=10, decimal_places=2)
    price_to_pay = models.DecimalField(validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('9999999.99'))], max_digits=9, decimal_places=2)
    
    published_date = models.DateTimeField(blank=False, null=True, default=timezone.now)
    end_date = models.DateTimeField(blank=False, null=True)
    
    on_bidding = models.BooleanField(blank=False, default=True)
    paid = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return self.name
    