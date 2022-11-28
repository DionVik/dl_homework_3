from django.db import models

# Create your models here.
def picture_path(instance, file):
    user_id = instance.id
    return 'avatar/user-{}/{}'.format(user_id, file)

def picture_path(instance, file):
    user_id = instance.id
    return 'picture/user-{}/{}'.format(user_id, file)

class User_profile(models.Model):
    name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 25)
    email = models.EmailField()
    phone = models.CharField(max_length = 11)
    birth_date = models.DateField(blank=True, null=True)
    avatar = models.ImageField(upload_to='media/', blank=True)
    
class Advertisment(models.Model):
    user = models.ForeignKey(User_profile, on_delete = models.CASCADE)
    category = models.CharField(max_length = 100)
    title = models.CharField(max_length = 100)
    content = models.TextField(blank=True)
    picture = models.ImageField(upload_to=picture_path, blank=True)
