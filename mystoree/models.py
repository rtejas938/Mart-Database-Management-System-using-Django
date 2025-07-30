from django.db import models

# Create your models here.

class Customer(models.Model):
    cname = models.CharField(max_length=50)
    cphoto = models.URLField(max_length=5000)
    cphone = models.CharField(max_length=10)
    caddress = models.CharField(max_length=200)

    def __str__(self):
        return f"(self.id) - (self.cname) - (self.phone)"


