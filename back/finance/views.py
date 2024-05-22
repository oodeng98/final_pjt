from django.shortcuts import render

import os
import requests
from openai import OpenAI
from rest_framework.decorators import api_view
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from .serializers import ExchangerateSerializer, ProductListSerializer, SubscribeSerializer
from .models import Product, User_Product, Question

FILE_PATH = os.path.join(os.path.dirname(__file__), 'train.txt')

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
  if request.method == 'GET':
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
      print(len(response))
    
      for res in response:
        for month in ('1', '3', '6', '12', '24', '36'):
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
            etc_note = res.get('etc_note'),
            save_trm = month,
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
            etc_note = res.get('etc_note'),
            save_trm = month,
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
          fin_prdt_cd = res.get('fin_prdt_cd'),
          save_trm = res.get('save_trm'),
        )[0]
        
        product.intr_rate_type = res.get('intr_rate_type')
        product.intr_rate_type_nm = res.get('intr_rate_type_nm')
        product.intr_rate = res.get('intr_rate')
        product.intr_rate2 = res.get('intr_rate2')
        
        if res.get('rsrv_type'):
          product.rsrv_type = res.get('rsrv_type')
          product.rsrv_type_nm = res.get('rsrv_type_nm')
        product.save()
    return Response(res, status=status.HTTP_200_OK)
  
@api_view(['GET'])
def get_product(request):
  if request.method == 'GET':
    products = Product.objects.all()
    serializers = ProductListSerializer(products, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
@login_required
def subscribe(request):
  if request.method == 'POST':
    product_id = request.data['product']
    product = Product.objects.get(pk=product_id)
    subscribes = User_Product.objects.filter(user=request.user, product=product)
    if subscribes:
      subscribes.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    else:
      serializer = SubscribeSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, product=product)
        return Response(status=status.HTTP_200_OK)
  elif request.method == 'GET':
    product_id = request.GET.get('product')
    product = Product.objects.get(pk=product_id)
    subscribes = User_Product.objects.filter(user=request.user, product=product_id)
    serializer = SubscribeSerializer(subscribes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def subscribe_list(request):
  if request.method == 'GET':
    subscribes = User_Product.objects.filter(user=request.user)
    serializer = SubscribeSerializer(subscribes, many=True)
    print(serializer.data)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
@api_view(['GET'])
def gpt(request):
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as f:
          file_content = f.read()
        f.close()
    except UnicodeDecodeError as e:
        return Response({'error': f'Unicode decode error: {str(e)}'}, status=500)

    if request.method == 'GET':
      prev_questions = [question.text for question in Question.objects.all().order_by('-created_at')[:1]]  
      query = request.GET.get('query')
      messages = [{
          "role": "user",
          "content": file_content + '위의 상품들 중에 검색을 하고 싶어.'
          }]
      for question in prev_questions + [query]:
        messages.append({
          "role": "user",
          "content": question
        })
      messages.append({
        "role": "user",
        "content": "마크다운 양식 없이 출력해줘."
        })
      
      client = OpenAI(api_key=settings.GPT_KEY)
      completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
        )
      Question.objects.create(text=query)
      return Response({'response': completion.choices[0].message.content})

#         completion = client.chat.completions.create(
#             model="gpt-4o",
#             messages=[
#                 {
#                     "role": "user",
#                     "content": '''
# 아래 예시를 보고 위 내용을 같은 형식으로 요약해줘

# 제주은행 - J정기예금 (만기지급식)
# 종류: 적금
# 가입 방법: 영업점, 인터넷, 스마트폰
# 우대 조건: 비대면 채널 가입 시 최고 0.5% 우대
# 가입 대상: 실명의 개인 및 개인사업자
# 저축 기간: 1, 3, 6, 12, 24, 36개월
# 저축 금리: 2% (1, 3개월), 3% (6개월 이상)
# 최고 우대 금리: 3% (6개월 이상)

# ''',
#                 },
#             ]
#         )
        # print()
        # return Response({'msg':completion})