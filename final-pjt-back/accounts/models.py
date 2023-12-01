from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=12, unique=True )
    nickname = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    
    USERNAME_FIELD = 'username'
    
    
class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        from allauth.account.utils import user_email, user_field, user_username
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        nickname = data.get("nickname")
        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if nickname:
            user_field(user, "nickname", nickname)
        if email:
            user_field(user, 'email', email)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user