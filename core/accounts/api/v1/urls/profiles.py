from django.urls import path, include
from ..views import *

urlpatterns = [

    # profile
    path('', ProfileApiView.as_view(), name='profile'),
]
