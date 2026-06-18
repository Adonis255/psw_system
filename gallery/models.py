from django.db import models
from django.contrib.auth.models import User

class PhotoItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/')
    photo_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    phone_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class PurchaseLog(models.Model):
    session_key = models.CharField(max_length=255)
    item = models.ForeignKey(PhotoItem, on_delete=models.CASCADE)
    purchased_photo = models.BooleanField(default=False)
    purchased_number = models.BooleanField(default=False)
    purchased_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.session_key} - {self.item.title}"