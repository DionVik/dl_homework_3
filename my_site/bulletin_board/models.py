from django.db import models

# Create your models here.
#def picture_path(instance, file):
    #user_id = instance.id
    #return 'avatar/user-{}/{}'.format(user_id, file)

#def picture_path(instance, file):
    #user_id = instance.id
    #return 'picture/user-{}/{}'.format(user_id, file)

class User_profile(models.Model):
    name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 25)
    email = models.EmailField()
    phone = models.CharField(max_length = 11)
    birth_date = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    
    def __str__(self):
        return f'{self.name} {self.last_name}'    
    
    
class Category(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return f'{self.name}'    
    
class Advertisment(models.Model):
    user = models.ForeignKey(User_profile, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.SET_DEFAULT, default = None)
    title = models.CharField(max_length = 100)
    content = models.TextField(max_length = 500)
    picture = models.ImageField(upload_to='pictures/', blank=True, null=True)
    
    def __str__(self):
        return f'{self.user} {self.title}'    