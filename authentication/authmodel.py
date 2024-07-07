from django.db import models
from common.utils import get_model_fields
from common import constants as ct

class UserAuthentication(models.Model):
    user_id = models.CharField(max_length=ct.CHAR_MEDIUM_LIMIT, primary_key=True)
    user_name = models.CharField(max_length=ct.CHAR_MEDIUM_LIMIT)
    email = models.EmailField(unique=True)
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return get_model_fields(UserAuthentication)

    class Meta:
        db_table = "user_authentication"