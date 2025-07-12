from django.urls import path, include
from .views import *


app_name = 'api-v1'

urlpatterns = [
    path('registraion/', RegistrationApiView.as_view(), name='registration'),
    path('token/login/', CustomObtainAuthToken.as_view(), name='token_login'),
]
