from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    #https://en.wikipedia.org/wiki/Database_index
    name = models.CharField(max_length=255,db_index=True)
    slug = models.SlugField(max_length=255,unique=True)
    
    # class Meta is optional additional data that are not fields
    class Meta:
        verbose_name_plural = 'categories'
    
    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])

    # to reference data by name
    def __str__(self):
        return self.name


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager,self).get_queryset().filter(is_active=True)
class Product(models.Model):
    # associate categories to the product, on_delete: deleting all products under that category
    category = models.ForeignKey(Category,related_name="product",on_delete=models.CASCADE)
    # associate product to user, on_delete all products for user
    created_by = models.ForeignKey(User, related_name="product_creator", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    # author of the book not the one that created the Product/Entry
    author = models.CharField(max_length=255,default="admin")
    description = models.TextField(blank=True)
    # we're not storing the image in the database, but storing the link to the image
    image = models.ImageField(upload_to="images/", default="images/default.png")
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    products = ProductManager()
    class Meta:
        verbose_name_plural = 'Products'
        # the - is for descending order
        ordering = ('-created',)
    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title