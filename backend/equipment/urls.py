from django.urls import path
from .views import test_api, upload_csv, upload_history, download_pdf
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("test/", test_api),
    path("upload/", upload_csv),
    path("history/", upload_history),

    # JWT AUTH
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # PDF download
    path("download/<str:filename>/", download_pdf),
]
