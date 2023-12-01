from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework import status

from django.forms.models import model_to_dict
from django.conf import settings 
from django.http import JsonResponse
from django.db.models import Max 
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from .serializers import DepositOptionsSerializers, DepositProductsSerializer, CommentSerializer, CategorySerializer
from .models import DepositOptions, DepositProducts, Comment, Category
import requests
# http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth=ae63b82d78387a034df270c1614ee229&topFinGrpNo=020000&pageNo=1

# 최초 데이터 받아올 함수
@api_view(['GET'])
def save_deposit_products(request , page):
    auth = settings.FINANCE_API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={auth}&topFinGrpNo=020000&pageNo={page}'
    response = requests.get(url).json()
    for li in response.get("result").get("baseList"):
        category_save = li.get('kor_co_nm')
        # print(category_save)
        category_data = {
            'kor_co_nm' : category_save
        }
        if not Category.objects.filter(kor_co_nm=category_save).exists():
            category_serializer = CategorySerializer(data=category_data)
            if category_serializer.is_valid(raise_exception=True):
                category_serializer.save()
        fin_prdt_cd = li.get('fin_prdt_cd')
        
        if not DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            save_products = {
                'fin_prdt_cd' : li.get('fin_prdt_cd'),
                'kor_co_nm' : li.get('kor_co_nm'),
                'fin_prdt_nm': li.get('fin_prdt_nm'),
                'etc_note' : li.get('etc_note'),
                'join_deny': li.get('join_deny'),
                'join_member': li.get('join_member'),
                'join_way': li.get('join_way'),
                'spcl_cnd': li.get('spcl_cnd')
            }
            serializer1 = DepositProductsSerializer(data=save_products)
            if serializer1.is_valid(raise_exception=True):
                serializer1.save()
            
    for li in response.get("result").get("optionList"):
        fin_prdt_cd = li.get('fin_prdt_cd')
        existing_option = DepositOptions.objects.filter(
            fin_prdt_cd = li.get('fin_prdt_cd'),
            intr_rate=li.get('intr_rate'),
            intr_rate2=li.get('intr_rate2'),
            save_trm=li.get('save_trm'),
        )
        # not 손대서 혹시 잘못되면 지우기
        if not existing_option.exists():
            save_options = {
                'product' : DepositProducts.objects.get(fin_prdt_cd = li.get("fin_prdt_cd")).pk,
                'fin_prdt_cd': li.get('fin_prdt_cd'),
                'intr_rate_type_nm': li.get('intr_rate_type_nm'),
                'intr_rate': li.get('intr_rate'),
                'intr_rate2': li.get('intr_rate2'),
                'save_trm': li.get('save_trm')
            }
            serializer2 = DepositOptionsSerializers(data=save_options)
            if serializer2.is_valid(raise_exception=True):
                serializer2.save()
    return JsonResponse({'message' : 'okay'})
    
    
# deposit 상품들 보여주세요
@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == 'GET':
        products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(products, many=True)
        return Response(serializer.data) 
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # raise_exception=True 설정하면 출력되지 않음
        return Response({'message' : '이미있는 데이터거나, 데이터가 잘못 입력되었습니다'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def deposit_bank_products_detail(request, kor_co_nm):
    product = DepositProducts.objects.filter(kor_co_nm=kor_co_nm)
    seiralizer = DepositProductsSerializer(product, many=True)
    return Response(seiralizer.data)


@api_view(['GET'])
def deposit_product_options(request, fin_prdt_cd):
    options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializers(options, many=True)
    return Response(serializer.data)
    

@api_view(['GET'])
def top_rate(reqeust):
    get_max = DepositOptions.objects.aggregate(intr_rate2=Max('intr_rate2'))
    options = DepositOptions.objects.get(intr_rate2=get_max['intr_rate2'])
    
    product = DepositProducts.objects.get(fin_prdt_cd=options.fin_prdt_cd)
    
    serializer1 = DepositOptionsSerializers(options)
    serializer2 = DepositProductsSerializer(product)
    
    to_show = {
        'deposit_product':serializer2.data,
        'options':serializer1.data,
    }
    
    return Response(to_show)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT' and comment.user != request.user:
        return Response({"detail": "You do not have permission to edit this comment."}, status=status.HTTP_403_FORBIDDEN)
    
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

# 유저 id도 같이 넣어야함
# 수정 필요
@api_view(['POST'])
@login_required
def comment_create(request, fin_prdt_cd):
    product = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(product=product, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    
@api_view(['GET'])
def get_comment_list(request, product_id):
    comment = Comment.objects.filter(product_id=product_id)
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data)


@api_view(['DELETE', 'PUT', 'GET'])
def control_comment(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        

@api_view(['GET'])
def get_category(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@login_required
def likes(request, fin_prdt_cd):
    product = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
    if request.user in product.like_users.all():
        product.like_users.remove(request.user)
    else :
        product.like_users.add(request.user)
    return JsonResponse({'result' : 'okay'})


@api_view(['GET'])
@login_required
def like_product(request):
    products = request.user.like_product.all()
    serializer = DepositProductsSerializer(products, many=True)
    return Response(serializer.data)

