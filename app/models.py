from django.db import models


# Create your models here.
class Input(models.Model):
    first_name=models.CharField(max_length=100)
    middle_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    mob_no=models.CharField(max_length=100 ,unique=True)
    user_name=models.CharField(max_length=100 ,unique=True)
    password=models.CharField(max_length=100 )
    confirm_password=models.CharField(max_length=100)
    email=models.EmailField(max_length=100 ,unique=True)

    def __str__(self):
        return self.first_name    

