from django.db import models
from django.utils import timezone

from accounts.models import CustomUser


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Advertisement(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True)
    publication_date = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return f'{self.user} {self.title}'