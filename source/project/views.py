from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Project, Contributor, Issue
from .serializers import ProjectSerializer, ContributorSerializer, IssueSerializer

from django.shortcuts import get_object_or_404



class ProjectList(ListAPIView, CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    
class ProjectDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView): 
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ContributorList(ListAPIView, CreateAPIView):
    
    def get_queryset(self):
        project = get_object_or_404(Project, id=self.kwargs['project_id'])
        queryset = Contributor.objects.filter(project_id=project)
        return queryset
    
    serializer_class = ContributorSerializer


class ContributorDelete(ListAPIView, DestroyAPIView):
    
    def get_queryset(self):
        queryset = Contributor.objects.filter(pk=self.kwargs['pk'])
        return queryset
    
    serializer_class = ContributorSerializer


class IssueList(ListAPIView, CreateAPIView):
    
    def get_queryset(self):
        project = get_object_or_404(Project, id=self.kwargs['project_id'])
        queryset = Issue.objects.filter(project_id=project)
        return queryset

    serializer_class = IssueSerializer

   
