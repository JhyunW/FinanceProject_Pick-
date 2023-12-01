from django.urls import path
from . import views

urlpatterns = [
    path('change-info/', views.changeUserInfo),
    path('get-user/<username>/', views.getUserInfo)
]
