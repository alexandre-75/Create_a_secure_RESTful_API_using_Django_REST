from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('accounts.urls')),
    path("api/projects/", include('project.urls')),
    path("api/token/", TokenObtainPairView.as_view(), name="obtain_tokens"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh_token")
]
