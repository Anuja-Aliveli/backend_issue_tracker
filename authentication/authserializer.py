from rest_framework import serializers
from common.utils import get_model_fields
from authentication.authmodel import UserAuthentication

class UserAuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAuthentication
        fields = get_model_fields(UserAuthentication)
        extra_kwargs = {
            'user_id': {'required': False},
            'email': {'required': False}
        }