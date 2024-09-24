from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_name=models.CharField(max_length=100)
    product_price=models.FloatField()
    stock=models.IntegerField()
    description=models.TextField()
    product_image=models.FileField(upload_to='static/uploads',null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='categories',null=True)

    def __str__(self):
        return self.product_name

class Chai(models.Model):
    CHAI_TYPE_CHOICE=[
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KT','KIWI'),
        ('PT','PLAIN'),
        ('ET','ELAICHI,')
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chais/')
    date=models.DateTimeField(default=timezone.now)
    types=models.CharField(max_length=2,choices=CHAI_TYPE_CHOICE)
    description=models.TextField(default='')

    def __str__(self):
        return self.name
    
# One to many
class ChaiReview(models.Model):
    chai=models.ForeignKey(Chai,on_delete=models.CASCADE,related_name='reviews')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='users')
    rating=models.IntegerField()
    comment=models.TextField()
    date_added=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'


# Many to many
class Store(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    chai_varieties=models.ManyToManyField(Chai,related_name='stores')

    def __str__(self):
        return self.name
    

# One to One
class Cerificate(models.Model):
    chai=models.OneToOneField(Chai,on_delete=models.CASCADE,related_name='certificates')
    certificate_number=models.CharField(max_length=100)
    issued_date=models.DateTimeField(default=timezone.now)
    valid_until=models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai.name}'

