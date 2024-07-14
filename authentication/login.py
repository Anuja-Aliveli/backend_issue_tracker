from authentication.authmodel import UserAuthentication
import jwt
from django.http import  JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status
from common import constants as ct
from django.conf import settings
from django.contrib.auth.hashers import check_password

@api_view(['POST'])
def user_login(request):
    user_name = request.data.get(ct.USER_NAME)
    password = request.data.get(ct.PASSWORD)
    try:
        user = UserAuthentication.objects.filter(user_name=user_name).get()
        if user:
            is_correct_password = check_password(password, user.password)
            if is_correct_password:
                # Generate JWT token
                payload = {'user_id': user.user_id}  # Customize payload as needed
                jwt_token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm='HS256')
                return JsonResponse({'message': ct.USER_LOGIN_SUCCESSFUL, 'token': jwt_token, 'user_name': user.user_name, 'email': user.email}, status=status.HTTP_200_OK)
            else:
                raise Exception(ct.LOGIN_INVALID_DATA_ERROR)
        else:
            raise Exception(ct.USER_NOT_FOUND)
    except Exception as error:
        return JsonResponse({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)