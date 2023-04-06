from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Project
from .serializers import ProjectSerializer

class ProjectList(ListAPIView, CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer