from django.urls import path, include
from ..views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    # regiristration
    path('registraion/', RegistrationApiView.as_view(), name='registration'),

    # chamne password
    path('change-password/', ChangePasswordApiView.as_view(), name='change_password'),

    # login token
    path('token/login/', CustomObtainAuthToken.as_view(), name='token_login'),
    path('token/logut/', CustomDiscardAuthToken.as_view(), name='token_logout'),

    # login jwt
    path('jwt/create/', CustomTokenObtainPairView.as_view(), name='jwt_create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt_verify'),
]
