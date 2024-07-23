from django.db import models

# Create your models here.
class Product(models.Model):
    x = [
        ("phone","phone"),
        ("tab","tab"),
        ("labtop","labtop"),
    ]
    name = models.CharField(max_length=50)
    content = models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.ImageField(upload_to='photos/%y/%m/%d', blank=True)
    activate = models.BooleanField(default=True)
    category = models.CharField(max_length=50,choices=x,default="cat",null=True)
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name="device"
        ordering=["price"]

