from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
#def picture_path(instance, file):
    #user_id = instance.id
    #return 'avatar/user-{}/{}'.format(user_id, file)

#def picture_path(instance, file):
    #user_id = instance.id
    #return 'picture/user-{}/{}'.format(user_id, file)


class UserProfile(models.Model):
    CITIES = [
        ('msc', 'Moscow'),
        ('tlt', 'Togliatti'),
        ('spb', 'Sankt Petersburg'),
        ('eka', 'Ekaterinburg')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    region = models.CharField(max_length=35, choices=CITIES)
    phone = models.CharField(max_length=11)
    birth_date = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.name}'    


class Advertisment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True)
    publication_date = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f'{self.user} {self.title}'
