from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=350)

    def __str__(self):
        return self.name


class Author(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.CharField(max_length=130)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)
    bio = models.CharField(max_length=300)

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    name = models.CharField(max_length=70)
    address = models.CharField(max_length=135)
    phone = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pages = models.IntegerField()
    cover = models.ImageField(upload_to='cover/', blank=True, null=True)
    description = models.CharField(max_length=350)
    
    def __str__(self):
        return self.title
    

class UserModel(models.Model):
    username = models.CharField(max_length=40, unique=True, null=False)
    phone = models.CharField(max_length=13, unique=True, null=False)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username
