from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    name = models.CharField(max_length=200)
    COLOR_CHOICES = (
    ("QIZIL", "qizil"),
    ("OQ", "oq"),
    ("QORA", "QORA"),
    )

    color = models.CharField(max_length=9,
                  choices=COLOR_CHOICES,
                  default="OQ")
                
    year = models.IntegerField()
    image = models.ImageField(upload_to='carimage/')
    like = models.IntegerField(default=0, null=True, blank=True)




    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Car"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='car_likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'car')



     
class Savat(models.Model):
    product = models.ForeignKey(Car, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    
        
    def __str__(self) -> str:
        return self.product.name
    
    class Meta:
        verbose_name_plural = 'Savat'
