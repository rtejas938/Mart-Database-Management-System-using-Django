from django.db import models

# Create your models here.

class Customer(models.Model):
    cname = models.CharField(max_length=50)
    cphoto = models.ImageField(upload_to='images/',default='default_image.jpg')
    cphone = models.CharField(max_length=10)
    caddress = models.CharField(max_length=200)

    def __str__(self):
        return self.cname
    

class Monthly(models.Model):
    name=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='mon',null=True,blank=True)
    january = models.DecimalField(max_digits=10,decimal_places=2)
    febraury = models.DecimalField(max_digits=10,decimal_places=2)
    march = models.DecimalField(max_digits=10,decimal_places=2)
    april = models.DecimalField(max_digits=10,decimal_places=2)
    may = models.DecimalField(max_digits=10,decimal_places=2)
    june = models.DecimalField(max_digits=10,decimal_places=2)
    july = models.DecimalField(max_digits=10,decimal_places=2)
    august = models.DecimalField(max_digits=10,decimal_places=2)
    september = models.DecimalField(max_digits=10,decimal_places=2)
    october = models.DecimalField(max_digits=10,decimal_places=2)
    november = models.DecimalField(max_digits=10,decimal_places=2)
    december = models.DecimalField(max_digits=10,decimal_places=2)