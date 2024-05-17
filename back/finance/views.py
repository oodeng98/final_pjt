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
        API_KEY = settings.EXCHANGE_RATE_API_KEY
        res = requests.get(
            url=URL, 
            params={
                'authkey': API_KEY,  
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
    ).json().get('result').get('baseList')
  
    for res in response:
      product = Product(
        category=idx,
        dcls_month = res.get('dcls_month'),
        fin_co_no = res.get('fin_co_no'),
        kor_co_nm = res.get('kor_co_nm'),
        fin_prdt_cd = res.get('fin_prdt_cd'),
        fin_prdt_nm = res.get('fin_prdt_nm'),
        join_way = res.get('join_way'),
        spcl_cnd = res.get('spcl_cnd'),
        join_deny = res.get('join_deny'),
        join_member = res.get('join_member'),
        )
    
    ans = Product.objects.filter(
        category=idx,
        dcls_month = res.get('dcls_month'),
        fin_co_no = res.get('fin_co_no'),
        kor_co_nm = res.get('kor_co_nm'),
        fin_prdt_cd = res.get('fin_prdt_cd'),
        fin_prdt_nm = res.get('fin_prdt_nm'),
        join_way = res.get('join_way'),
        spcl_cnd = res.get('spcl_cnd'),
        join_deny = res.get('join_deny'),
        join_member = res.get('join_member'),
        )
    if not ans:
      product.save()
    
  for idx, category in enumerate(['deposit', 'saving']):
    API_URL = f'http://finlife.fss.or.kr/finlifeapi/{category}ProductsSearch.json'
    
    response = requests.get(
      url=API_URL,
      params=params
    ).json().get('result').get('optionList')
  
    for res in response:
      product = Product.objects.filter(
        category=idx,
        dcls_month = res.get('dcls_month'),
        fin_co_no = res.get('fin_co_no'),
        fin_prdt_cd = res.get('fin_prdt_cd')
      )[0]
      product.intr_rate_type = res.get('intr_rate_type')
      product.intr_rate_type_nm = res.get('intr_rate_type_nm')
      product.save_trm = res.get('save_trm')
      product.intr_rate = res.get('intr_rate')
      product.intr_rate2 = res.get('intr_rate2')
      product.save()
  return Response(res)
  

@api_view(['GET'])
def get_product(request):
  products = Product.objects.all()
  serializers = ProductListSerializer(products, many=True)
  return Response(serializers.data)
