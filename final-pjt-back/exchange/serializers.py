from rest_framework import serializers
from .models import Exchange

class exchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = '__all__'
        
        
class kftc_bkprSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields = ('cur_unit', 'cur_nm', 'date_field', 'kftc_bkpr')