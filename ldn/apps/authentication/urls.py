from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from .views import (
    UserRegistrationView,
    LogoutAndBlacklistRefreshTokenForUserView,
    GetTokenWithRoleView,
    UserProfileView,
)

urlpatterns = [
    path("user/register/", UserRegistrationView.as_view(), name="register"),
    path(
        "user/login/", GetTokenWithRoleView.as_view(), name="token_obtain_pair"
    ),
    path(
        "token/refresh/",
        jwt_views.TokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path(
        "token/blacklist/",
        LogoutAndBlacklistRefreshTokenForUserView.as_view(),
        name="blacklist",
    ),
    path("user/<pk>/", UserProfileView.as_view(), name="profile"),
]