from django.urls import path
from accounts.views import SignupView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
     path('signup/', SignupView.as_view(), name='accounts-signup'),
     path("login/", TokenObtainPairView.as_view(), name="login_obtain_tokens"),
]
