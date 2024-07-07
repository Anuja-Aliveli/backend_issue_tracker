from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from common import constants as ct
from rest_framework import status
from authentication.authmodel import UserAuthentication
from authentication.authserializer import UserAuthenticationSerializer
from common.utils import generate_id, get_latest_id
from django.contrib.auth.hashers import make_password

# Password Validations
def validate_password(password):
    check_password = False
    if len(password) < 6:
        raise Exception(ct.PASSWORD_LENGTH_ERROR)
    else:
        number_count = 0
        small_letter_count = 0
        caps_count = 0
        symbol_count = 0
        for letter in password:
            if letter.isupper():
                caps_count += 1
            elif letter.islower():
                small_letter_count += 1 
            elif letter.isdigit():
                number_count += 1
            else:
                symbol_count += 1
        if number_count == 0 and small_letter_count == 0 and caps_count == 0 and symbol_count == 0:
            raise Exception(ct.PASSWORD_TYPES_ERROR)
        elif caps_count == 0:
            raise Exception(ct.PASSWORD_CAPITAL_ERROR)
        elif symbol_count == 0:
            raise Exception(ct.PASSWORD_SYMBOL_ERROR)
        elif number_count == 0:
            raise Exception(ct.PASSWORD_NUMBER_ERROR)
        else:
            check_password = True
    return check_password

# Email Validations
def validate_user_email(email):
    check_email = False
    if email is None:
        raise Exception(ct.EMAIL_INVALID_ERROR)
    else:
        email_domain = ''
        try:
            validate_email(email)
            email_domain = email.split('@')[1].split('.')[0]
        except ValidationError:
            raise Exception(ct.EMAIL_INVALID_ERROR)
        if email_domain not in ct.user_mail_domains_allowed:
            raise Exception(ct.EMAIL_INVALID_DOMAIN_ERROR)
        elif UserAuthentication.objects.filter(email=email).exists():
            raise Exception(ct.EMAIL_USER_ALREADY_EXITS_ERROR)
        else:
            check_email = True
    return check_email

@api_view(['POST'])
def user_registration(request):
    email = request.data.get(ct.EMAIL, None)
    password = request.data.get(ct.PASSWORD, None)
    user_name = request.data.get(ct.USER_NAME, None)
    try:
        is_valid_email = validate_user_email(email)
        is_valid_password = validate_password(password)
        if is_valid_email and is_valid_password:
            latest_user = get_latest_id(UserAuthentication, 'user_id')
            user_data = {
                'email': email,
                'password': make_password(password),
                'user_id': generate_id(ct.USER_ID,latest_user),
                'user_name': user_name
            }
            serializer = UserAuthenticationSerializer(data=user_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'message': ct.USER_REGISTER_SUCCESSFUL}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return JsonResponse({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)
    