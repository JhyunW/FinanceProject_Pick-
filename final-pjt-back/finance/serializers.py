from rest_framework import serializers
from .models import DepositProducts, DepositOptions, Comment, Category
from django.contrib.auth import get_user_model

class DepositProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepositProducts
        fields = '__all__'
        read_only = ('like_users',)


class DepositOptionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = DepositOptions
        fields = '__all__'
        read_only = ('fin_prdt_cd',)
        

class CommentSerializer(serializers.ModelSerializer):
    class DepositProductsSerializer(serializers.ModelSerializer):
        class Meta:
            model = DepositProducts
            fields = ('pk', 'fin_prdt_cd',)
    
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('id', 'nickname')
            
    user = UserSerializer(read_only=True) 
    product = DepositProductsSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'