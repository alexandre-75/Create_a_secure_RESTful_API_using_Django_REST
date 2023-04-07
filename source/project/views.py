from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Project, Contributor, Issue, Comment
from .serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer

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
    serializer_class = IssueSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        queryset = Issue.objects.filter(project=project_id)
        return queryset



class IssueDetail(RetrieveAPIView, DestroyAPIView, UpdateAPIView):
    
    def get_queryset(self):
        queryset = Issue.objects.filter(pk=self.kwargs['pk'])
        return queryset

    serializer_class = IssueSerializer


class CommentList(ListAPIView, CreateAPIView):
    
    def get_queryset(self):
        issue_id = self.kwargs.get('issue_id')
        queryset = Comment.objects.filter(issue=issue_id)
        return queryset
    
    serializer_class = CommentSerializer

class CommentDetail(RetrieveAPIView, DestroyAPIView, UpdateAPIView):
    
    def get_queryset(self):
        queryset = Comment.objects.filter(pk=self.kwargs['pk'])
        return queryset

    serializer_class = CommentSerializer