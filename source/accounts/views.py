from .models import User
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import SignupSerializer
from rest_framework.permissions import AllowAny


class SignupView(ListAPIView, CreateAPIView):

    """
    A view that allows users to sign up by creating new user objects.
    Inherits from ListAPIView and CreateAPIView to enable listing and creating user objects.
    Uses the SignupSerializer to serialize and deserialize user data.
    Allows any user, including unauthenticated users, to access the view by setting the permission_classes attribute to [AllowAny].
    """

    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]
