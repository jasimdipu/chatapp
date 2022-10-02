from django.contrib import admin
from django.urls import path, include, re_path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(
        "api/v1/schema/user/", include(("users.urls", "users")),
    ),
    re_path(
        "api/v1/schema/chat/", include(("chat.urls", "chat")),
    ),

    # YOUR PATTERNS
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path("api/v1/schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name='schema'), name="swagger-ui"),
    path("api/v1/schema/redoc", SpectacularRedocView.as_view(url_name='schema'), name="redoc"),
]
