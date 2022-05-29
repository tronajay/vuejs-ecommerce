from django.urls import path
from .views import UserAPIViewSet, UserAddressViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path(
        'login/', 
        TokenObtainPairView.as_view(), 
        name='token_obtain_pair'),
    path(
        'register/', 
        UserAPIViewSet.as_view({"post":"create"}),
        name="user_register_api_view"
        ),
    path(
        'token/refresh/', 
        TokenRefreshView.as_view(), 
        name='token_refresh'
        ),
    path(
        "address/",
        UserAddressViewSet.as_view({"get":"get_address","post":"create"}),
        name="get_saved_address_for_users"
    ),
]