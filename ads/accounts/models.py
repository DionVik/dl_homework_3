from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    CITIES = [
        ('msc', 'Moscow'),
        ('tlt', 'Togliatti'),
        ('eka', 'Ekaterinburg')
    ]
    region = models.CharField(max_length=35, choices=CITIES)
    phone = models.CharField(max_length=11)
    birth_date = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

