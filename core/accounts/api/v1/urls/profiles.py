from django.urls import path

from ..views import *

urlpatterns = [
    # profile
    path("", ProfileApiView.as_view(), name="profile"),
]
