from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class CousUserManager(BaseUserManager):
    def create_user(self, nickname, kakao_sub, password=None):
        if not kakao_sub:
            raise ValueError('User must have a kakao_sub')
        
        user = self.model(
            kakao_sub=kakao_sub,
        )
        user.nickname = nickname
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, nickname, kakao_sub, password=None):
        if not kakao_sub:
            raise ValueError('User must have a kakao_sub')
        
        user = self.model(
            kakao_sub=kakao_sub,
        )
        user.is_admin = True
        user.nickname = nickname
        user.set_password(password)
        user.save()
        return user
    
class CousUser(AbstractBaseUser):
    nickname = models.CharField(max_length=1024, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    kakao_sub = models.CharField(max_length=1024, unique=True)

    objects = CousUserManager()

    USERNAME_FIELD = 'kakao_sub'
    # REQUIRED_FIELDS = ['nickname']

    @property
    def is_staff(self):
        return self.is_admin