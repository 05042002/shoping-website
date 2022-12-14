from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500, default="")
    phone = models.CharField(max_length=50, default="")


    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    item_json =models.CharField(max_length=15000)
    name= models.CharField(max_length=111)
    email=models.CharField(max_length=111)
    address=models.CharField(max_length=5000)
    phone=models.CharField(max_length=5000,default="")
    city=models.CharField(max_length=5000)
    state=models.CharField(max_length=111)
    zip_code=models.CharField(max_length=500)