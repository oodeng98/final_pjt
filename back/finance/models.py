from django.db import models
from django.conf import settings

# Create your models here.
class Exchangerate(models.Model):
  bkpr = models.FloatField()
  cur_nm = models.CharField(max_length=16)
  cur_unit = models.CharField(max_length=16)
  deal_bas_r = models.FloatField()
  kftc_bkpr = models.FloatField()
  kftc_deal_bas_r = models.FloatField()
  ten_dd_efee_r = models.IntegerField()
  ttb = models.FloatField()
  tts = models.FloatField()


class Product(models.Model):
  category = models.IntegerField()  # 0은 예금, 1은 적금
  # 추후 더 추가


class User_Product(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  product = models.ForeignKey("Product", on_delete=models.CASCADE)
  balance = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
