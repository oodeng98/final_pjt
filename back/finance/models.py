from django.db import models
from django.conf import settings

# Create your models here.
class Exchangerate(models.Model):
  # 추후 더 추가
  pass


class Product(models.Model):
  category = models.IntegerField()  # 0은 예금, 1은 적금
  # 추후 더 추가
  
class User_Product(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  product = models.ForeignKey("Product", on_delete=models.CASCADE)
  balance = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
