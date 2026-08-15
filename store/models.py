from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_user')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products_category')
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='products/')
    bio = models.TextField(blank=True, null=True)
    stock = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_product