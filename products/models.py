from django.db import models
from datetime import datetime
# Create your models here.
class Product(models.Model):
    x = [
        ("cat","cat"),
        ("dog","dog")
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
        verbose_name="name"
        ordering=["price"]

class Test(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True)
    created = models.DateTimeField(default=datetime.now)