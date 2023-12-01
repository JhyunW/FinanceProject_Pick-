from rest_framework import serializers

from django.contrib.auth import get_user_model
from allauth.account import app_settings as allauth_settings
from allauth.utils import get_username_max_length
from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer

User = get_user_model()

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model : User
        fields = ('pk', 'username', 'nickname', 'email')
        


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(
        required = False,
        allow_blank = True,
        max_length = 12
    )
    def get_cleaned_data(self):
        return {
            'email' : self.validated_data.get('email', ''),
            'username' : self.validated_data.get('username', ''),
            'nickname' : self.validated_data.get('nickname', ''),
            'password1' : self.validated_data.get('password1', ''),
        }
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user
    
    
class modifyUserdata(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('email', 'nickname')