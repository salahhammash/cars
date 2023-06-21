from django.db import models
from accounts.models import CustomUser
from django.urls import reverse


class Car(models.Model):
    name = models.CharField(max_length=255,null=False)
    price = models.IntegerField(null=False,blank=True)
    desc = models.TextField(null=False,blank=True)
    purchaser = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('cars_list')