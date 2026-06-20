from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.
class Item (models.Model):
    def __str__(self):
        return self.item_name
    user_name=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    item_name=models.CharField(max_length=200)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField()
    item_image=models.CharField(max_length=500,default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT27gTKHqKhHk3i-EiarE5Q9IND_awvKaKjxw&s")


def get_absolute_url(self):
    return reverse ("food:detail",kwargs={"pk":self.pk})