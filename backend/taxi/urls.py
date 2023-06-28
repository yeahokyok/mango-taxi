from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views import SignUpView, LoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/signup/", SignUpView.as_view(), name="sign_up"),
    path("api/login/", LoginView.as_view(), name="login"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(
        "api/trip/",
        include(
            "trips.urls",
            "trip",
        ),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
