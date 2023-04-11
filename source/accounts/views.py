from .models import User
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import SignupSerializer
from rest_framework.permissions import AllowAny


class SignupView(ListAPIView, CreateAPIView):
    
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]