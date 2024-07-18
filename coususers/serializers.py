from rest_framework import serializers

from coususers.models import CousUser

class CousUserResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CousUser
        fields = ['nickname', 'kakao_sub']
        extra_kwargs = {
            field: {'read_only': True} for field in fields
        }

class KakaoLoginRequestSerializer(serializers.Serializer):
    access_code = serializers.CharField()
    
class CousUserPatchSerializer(serializers.Serializer):
    nickname = serializers.CharField()