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
  dcls_month = models.TextField()  # 공시 제출월(option)
  fin_co_no = models.TextField()  # 금융회사 코드(option)
  kor_co_nm = models.TextField()  # 금융회사 명
  fin_prdt_cd = models.TextField()  # 금융상품 코드(option)
  fin_prdt_nm = models.TextField()  # 금융상품 명
  join_way = models.TextField()  # 가입 방법
  spcl_cnd = models.TextField()  # 우대조건
  join_deny = models.TextField()  # 가입제한
  join_member = models.TextField()  # 가입대상

  intr_rate_type = models.TextField(null=True)  # 저축 금리 유형
  intr_rate_type_nm = models.TextField(null=True)  # 저축 금리 유형명
  save_trm = models.TextField(null=True)  # 저축 기간
  intr_rate = models.IntegerField(null=True)  # 저축 금리
  intr_rate2 = models.IntegerField(null=True)  # 최고 우대 금리

class User_Product(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  product = models.ForeignKey("Product", on_delete=models.CASCADE)
  balance = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)