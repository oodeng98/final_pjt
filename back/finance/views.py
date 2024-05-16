from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from pprint import pprint
from .serializers import ExchangerateSerializer

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