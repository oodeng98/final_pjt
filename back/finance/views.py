from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from .serializers import ExchangerateSerializer
from django.conf import settings

from .models import Product
from .serializers import ProductListSerializer

# Create your views here.
@api_view(['GET'])
def exchange_rate(request):
    if request.method == 'GET':
        URL = 'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
        res = requests.get(
            url=URL, 
            params={
                'authkey': 'voy59yWzqPBxQQBkmToyj9CjZMfaIOHG', 
                'data': 'AP01'
            }
        )
        data = res.json()
        for i in range(len(data)):
            info = data[i]
            for key in ['bkpr', 'deal_bas_r', 'kftc_bkpr', 'kftc_deal_bas_r', 'ten_dd_efee_r', 'ttb', 'tts', 'yy_efee_r']:
                if key == 'result':
                    continue
                info[key] = info[key].replace(',', '')
                info[key] = float(info[key])
        serializer = ExchangerateSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def save(request):
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
  products = Product.objects.all()
  serializers = ProductListSerializer(products, many=True)
  return Response(serializers.data)
