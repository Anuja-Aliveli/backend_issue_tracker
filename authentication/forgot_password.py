from rest_framework.decorators import api_view
from rest_framework import status
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from authentication.authmodel import UserAuthentication
from authentication.authserializer import UserAuthenticationSerializer
from common.constants import EMAIL, PASSWORD

@api_view(['GET'])
def forgot_login_password(request):
    email = request.query_params.get(EMAIL)
    try:
        user = UserAuthentication.objects.filter(email=email).first()
        if user:
            return JsonResponse({'user_email_found': True}, status=status.HTTP_200_OK)
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