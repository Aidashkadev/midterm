from django.db import models
class Contact(models.Model):
    laste_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    photo = models.ImageField(upload_to='', blank=True, null=True)
    birth_date = models.DateField()

def __str__(self):
    return f"{self.last_name} {self.first_name}"

    
# Create your models here.
