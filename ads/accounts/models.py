from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.


class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class CustomUser(AbstractUser):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default=None, blank=True, null=True)
    phone = models.CharField(max_length=11, verbose_name="Phone",
                             help_text="Required", default="-")
    avatar = models.ImageField(upload_to='avatars/', blank=True,
                               null=True, help_text="Not required")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('accounts:profile', args=[str(self.id)])



