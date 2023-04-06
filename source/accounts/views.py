from .models import User
from rest_framework.generics import CreateAPIView
from .serializers import SignupSerializer
from rest_framework.permissions import AllowAny


class SignupView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = SignupSerializer
