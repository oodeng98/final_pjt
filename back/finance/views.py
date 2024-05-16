from django.shortcuts import render
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import api_view

import requests
from .models import Product
from .serializers import ProductListSerializer

# Create your views here.
def save():
  params = {
    'auth': settings.FINANCE_API_KEY,
    'topFinGrpNo': '020000',
    'pageNo': '1'
  }
  
  for idx, category in enumerate(['deposit', 'saving']):
    API_URL = f'http://finlife.fss.or.kr/finlifeapi/{category}ProductsSearch.json'
    
    response = requests.get(
      url=API_URL,
      params=params
    ).json().get('result').get('optionList')
  
    for res in response:
      product = Product(
        category=idx,
        fin_co_no = res.get('fin_co_no'),
        fin_prdt_cd = res.get('fin_prdt_cd'),
        intr_rate_type = res.get('intr_rate_type'),
        save_trm = res.get('save_trm'),
        intr_rate = res.get('intr_rate'),
        intr_rate2 = res.get('intr_rate2'),
        )
      ans = Product.objects.filter(
        category=idx,
        fin_co_no = res.get('fin_co_no'),
        fin_prdt_cd = res.get('fin_prdt_cd'),
        intr_rate_type = res.get('intr_rate_type'),
        save_trm = res.get('save_trm'),
        intr_rate = res.get('intr_rate'),
        intr_rate2 = res.get('intr_rate2'),
      )
      if not ans:
        product.save()


@api_view(['GET'])
def get_product(request):
  save()
  products = Product.objects.all()
  serializers = ProductListSerializer(products, many=True)
  return Response(serializers.data)