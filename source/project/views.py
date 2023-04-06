from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Project
from .serializers import ProjectSerializer

class ProjectList(ListAPIView, CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    
class ProjectDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView): 
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
