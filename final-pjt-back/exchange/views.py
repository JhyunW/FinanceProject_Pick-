from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings

from .models import Exchange
from .serializers import exchangeSerializer, kftc_bkprSerializer

from datetime import datetime
import requests



# Create your views here.
# 날짜를 입력받아 그 날짜의 데이터를 요청
api_view(['GET'])
def save_exchange(request, date):
    requestDate = date
    API_KEY=settings.EXCHANGE_API_KEY
    url = f'https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey={API_KEY}&searchdate={requestDate}&data=AP01'
    response = requests.get(url).json()
    exchangeObject = Exchange.objects.filter(date_field=requestDate)
    if not exchangeObject.exists():
        for res_data in response:
            if (res_data.get('cur_unit') == "EUR" or res_data.get('cur_unit') == "CNH" or res_data.get('cur_unit') == "JPY(100)" or res_data.get('cur_unit') == "USD"):
                exchange_info = {
                    'result' : res_data.get('result'), 
                    'cur_unit' : res_data.get('cur_unit'), 
                    'ttb' : res_data.get('ttb'), 
                    'tts' : res_data.get('tts'),  
                    'deal_bas_r' : res_data.get('deal_bas_r'), 
                    'bkpr' : res_data.get('bkpr'),  
                    'yy_efee_r' : res_data.get('yy_efee_r'),  
                    'ten_dd_efee_r' : res_data.get('ten_dd_efee_r'),  
                    'kftc_bkpr' : res_data.get('kftc_bkpr'),  
                    'kftc_deal_bas_r' : res_data.get('kftc_deal_bas_r'),  
                    'cur_nm' : res_data.get('cur_nm'),  
                    'date_field' : date
                }  
                serializer = exchangeSerializer(data=exchange_info)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
    return JsonResponse({'message' : 'okay'})


# 현재 날짜를 기준으로 엔/유로/달러/위안의 환율을 반환
@api_view(['GET'])
def get_exchange(request):
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    reqeustDay = f'{year}{month}{day}'
    # reqeustDay = '20231120'
    
    exchange_info = Exchange.objects.filter(date_field = reqeustDay)
    if not exchange_info.exists():
        save_exchange(request, reqeustDay)
        exchange_info = Exchange.objects.filter(date_field = reqeustDay)
        
    serializer = kftc_bkprSerializer(exchange_info, many=True)
    return Response(serializer.data) 