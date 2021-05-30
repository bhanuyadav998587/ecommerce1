from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    img = models.ImageField(upload_to = '')

    def __str__(self):
        return self.title

class Cart(models.Model):
    cart_id=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    quantity=models.IntegerField()
    timestamp=models.DateTimeField(auto_now=True)
    product=models.ForeignKey(Product ,on_delete = models.PROTECT)
    def __str__(self):
         return self.product


    def update_quantity(self,request):
        self.quantity=self.quantity+1
        self.save()

    def total(self):
        return self.quantity*self.price

User = get_user_model()

class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', 
                                on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(unique=True, max_length=100, null=True, blank=True)
    checksum = models.CharField(max_length=100, null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.order_id is None and self.made_on and self.id:
            self.order_id = self.made_on.strftime('PAY2ME%Y%m%dODR') + str(self.id)
        return super().save(*args, **kwargs)

