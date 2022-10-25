from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

CATEGORY_CHOICES = (
    ('El','Electronics'),
    ('Re','Real Estate'),
    ('Bk','Books'),
    ('He','Health'),
    ('Ga','Gadgets'),
    ('Co','Cosmetics'),
    ('Ag','Agri products'),
    ('Ww','Women wear'),
    ('Mw','Men wear'),
    ('Kw','Kids wear')
)

# Create your models here.
class Items(models.Model):
    item_title = models.CharField(max_length=150)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    item_description = models.CharField(max_length=250, blank=False, null=False)
    item_price = models.FloatField()
    item_disc_price = models.FloatField(blank=True, null=True)
    item_image = models.ImageField(default='default.jpg',upload_to='product_img',blank=False,null=False)
    date_posted= models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User,on_delete= models.CASCADE)

    def __str__(self):
        return self.item_title

    '''def save(self):
        super().save()

        img = Image.open(self.item_image.path)

        if img.height > 400 or img.width > 400:
            output_size=(400,400)
            img.thumbnail(output_size)
            img.save(self.item_image.path)'''
    
    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)
        img = Image.open(self.item_image.path)
        
        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.item_image.path)

class OrderItem(models.Model):
    item = models.ForeignKey(Items, on_delete= models.CASCADE)

    def __str__(self):
        return self.title 

class Order(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    item = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    