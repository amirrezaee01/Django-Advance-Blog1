from rest_framework import generics
from rest_framework.response import Response
from .serializer import *
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from ...models import Profile
from mail_templated import send_mail, EmailMessage
from ..utils import EmailThread
from rest_framework_simplejwt.tokens import RefreshToken
from jwt import ExpiredSignatureError, InvalidSignatureError, DecodeError
import jwt
from django.conf import settings
User = get_user_model()


class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            email = serializer.validated_data['email']
            data = {'email': email}

            user_obj = get_object_or_404(User, email=email)
            token = self.get_tokens_for_user(user_obj)

            email_obj = EmailMessage(
                'email/activation_email.tpl',
                {'token': token},
                'amir@gmail.com',
                to=[email]
            )
            EmailThread(email_obj).start()

            return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class CustomObtainAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class ChangePasswordApiView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not user.check_password(serializer.validated_data['old_password']):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST
                )

            user.set_password(serializer.validated_data['new_password'])
            user.save()

            return Response({
                "email": user.email,
                "message": "Password changed successfully."
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileApiView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)
        return obj


class TestEmailSend(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        self.email = "sajadrezaee@gmail.com"
        user_obj = get_object_or_404(User, email=self.email)
        token = self.get_tokens_for_user(user_obj)
        email_obj = EmailMessage('email/hello.tpl', {'token': token}, 'amir@gmail.com',
                                 to=['sajadrezaee@gmail.com'])
        EmailThread(email_obj).start()
        return Response('email sent', status=status.HTTP_200_OK)

    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)


class ActivationApiView(APIView):
    def get(self, request, token, *args, **kwargs):
        try:
            token = jwt.decode(token, settings.SECRET_KEY,
                               algorithms=['HS256'])
            user_id = token.get('user_id')
        except ExpiredSignatureError:
            return Response({'error': 'Activation link has expired.'}, status=status.HTTP_400_BAD_REQUEST)
        except InvalidSignatureError:
            return Response({'error': 'Invalid activation link.'}, status=status.HTTP_400_BAD_REQUEST)
        except DecodeError:
            return Response({'error': 'Invalid activation link.'}, status=status.HTTP_400_BAD_REQUEST)
        user_obj = User.objects.get(pk=user_id)
        if user_obj.is_verified:
            return Response({'message': 'User is already verified.'}, status=status.HTTP_200_OK)
        user_obj.is_verified = True
        user_obj.save()
        return Response({'message': 'User activated and verified successfully.'}, status=status.HTTP_200_OK)
