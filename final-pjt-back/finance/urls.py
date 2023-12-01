from django.urls import path
from . import views
# 금융상품 관련 필요한 정보들 요청시킬 url
# 1. 금융상품 전체 목록 조회시킬 url
# 2. 필요한 금융상품(id)만 가져와서 전달해줄 url
# 필요한게 더 있어 보이면 그때가서 일단 추가

urlpatterns = [
    path('get-product-category/', views.get_category),
    path('save-deposit-products/<page>/', views.save_deposit_products),
    path('deposit-products/', views.deposit_products),
    path('deposit-products/<str:kor_co_nm>/', views.deposit_bank_products_detail),       # 은행별로 리스트 모아오기
    path('deposit-product-options/<str:fin_prdt_cd>/', views.deposit_product_options),
    path('top-rate/', views.top_rate),
    path('get-comment-list/<int:product_id>/', views.get_comment_list),             # product_id와 관련된 모든 댓글 가져오기
    path('comments/<int:comment_pk>/', views.comment_detail),                       # 'GET', 'DELETE', 'PUT'
    path('product/<fin_prdt_cd>/comments/', views.comment_create),                  # fin_prdt_dc를 가지는 상품에 댓글 달기
    path('product/<fin_prdt_cd>/likes/', views.likes),
    path('like-product/', views.like_product),
]
