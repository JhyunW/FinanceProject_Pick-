from django.urls import path
from . import views

urlpatterns = [
    path('save-exchange/<date>/', views.save_exchange),
    path('get-exchange/', views.get_exchange),
]
