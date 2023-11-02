from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    stock_count=models.IntegerField(default=0, help_text="how many items are currently in stock")
    price=models.DecimalField(max_digits=6, decimal_places=2)
    description=models.TextField(default="", blank=True)
    sku=models.CharField(verbose_name="Stock Keeping Unit",max_length=20, unique=True)

class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

class Categorie(models.Model):
    name=models.CharField(max_length=100)
    Products = models.ManyToManyField('Product',related_name='categories')

    def __str__(self):
        return self.name
