from django.db import models

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




    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = "Car"



