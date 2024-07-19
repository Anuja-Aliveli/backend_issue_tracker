from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from authentication.authmodel import UserAuthentication
from authentication.authserializer import UserAuthenticationSerializer
from common.constants import EMAIL, PASSWORD, VERIFICATION_CODE_TEXT
from django.utils.crypto import get_random_string

from common.utils import send_email
from communication.email_template import get_verification_code_message

def send_email_forgot_password(user_name, email, verification_code):
    subject = VERIFICATION_CODE_TEXT
    message = get_verification_code_message(user_name, verification_code)
    to_user = email
    send_email(subject, message, to_user)


@api_view(['GET'])
def check_email(request):
    email = request.query_params.get(EMAIL)
    try:
        user = UserAuthentication.objects.filter(email=email).get()
        if user:
            verification_code = get_random_string(length=6, allowed_chars='1234567890')
            send_email_forgot_password(user.user_name, user.email, verification_code)
            return JsonResponse({'user_email_found': True, 'verification_code': verification_code}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'user_email_found': False}, status=status.HTTP_404_NOT_FOUND)
    except UserAuthentication.DoesNotExist:
        return JsonResponse({'user_email_found': False}, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def reset_forgot_password(request):
    email = request.data.get(EMAIL)
    password = request.data.get(PASSWORD)
    try:
        user = UserAuthentication.objects.get(email=email)
        password = make_password(password)
        serializer = UserAuthenticationSerializer(instance=user, data={'password': password})
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except UserAuthentication.DoesNotExist:
        return JsonResponse({'user_email_found': False}, status=status.HTTP_404_NOT_FOUND)

@api_view(["GET"])
def test_jwt_verfication_api(request):
    email = request.query_params.get(EMAIL, None)
    print(email)
    return JsonResponse({'message': 'Hello'})