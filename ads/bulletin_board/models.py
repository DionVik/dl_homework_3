from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model

from accounts.models import CustomUser


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name of category")

    def __str__(self):
        return f'{self.name}'


class Advertisement(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="ads")
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100, verbose_name="Title")
    content = models.TextField(max_length=500, verbose_name="Content")
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True, verbose_name="Picture")
    publication_date = models.DateField(default=timezone.now, verbose_name="Date of publication")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Price, rub")

    def __str__(self):
        return f'{self.author} {self.title}'

    def get_absolute_url(self):
        return reverse('ad', args=[str(self.id)])


