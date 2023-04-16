from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from .models import Project, Contributor, Issue, Comment
from .serializers import ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer
from .permissions import ProjectPermissions, ContributorPermissions, CommentIssuePermissions
from rest_framework.permissions import IsAuthenticated


"""
    The rest_framework.generics module contains generic classes to facilitate the creation of common Django REST Framework (DRF) views.
    The five classes are generic views that perform CRUD (Create, Read, Update, Delete) operations for DRF models.

    ListAPIView: this generic view allows to retrieve a list of objects from a DRF model.
    CreateAPIView: this generic view allows to create a new object for a DRF model.
    RetrieveAPIView: This generic view allows retrieving a specific object from a DRF model.
    UpdateAPIView: this generic view allows to update a specific object for a DRF model.
    DestroyAPIView: This generic view allows to delete a specific object from a DRF model.
"""


class ProjectList(ListAPIView, CreateAPIView):

    """
    API endpoint that allows listing and creation of projects.

    Inherits from ListAPIView and CreateAPIView.
    Requires authentication (IsAuthenticated permission) to access.
    Uses the ProjectSerializer for serialization.
    Returns a queryset of all Project objects in the database.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectDetail(RetrieveAPIView, UpdateAPIView, DestroyAPIView):

    """
    API endpoint that allows retrieval, update and deletion of a project.

    Inherits from RetrieveAPIView, UpdateAPIView and DestroyAPIView.
    Requires authentication (IsAuthenticated permission) and ProjectPermissions to access.
    Uses the ProjectSerializer for serialization.
    Returns a queryset of the specified Project object.
    """

    permission_classes = [ProjectPermissions, IsAuthenticated]
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ContributorList(ListAPIView, CreateAPIView):

    """
    API endpoint that allows listing and creation of contributors for a project.

    Inherits from ListAPIView and CreateAPIView.
    Requires authentication (IsAuthenticated permission) and ProjectPermissions to access.
    Uses the ContributorSerializer for serialization.
    Returns a queryset of all Contributor objects for the specified project.
    """

    permission_classes = [ProjectPermissions, IsAuthenticated]
    serializer_class = ContributorSerializer

    def get_queryset(self):
        project = self.kwargs.get('project_id')
        queryset = Contributor.objects.filter(project_id=project)
        return queryset


class ContributorDelete(ListAPIView, DestroyAPIView):

    """
    API endpoint that allows deletion of a contributor for a project.

    Inherits from ListAPIView and DestroyAPIView.
    Requires authentication (IsAuthenticated permission) and ProjectPermissions to access.
    Uses the ContributorSerializer for serialization.
    Returns a queryset of the specified Contributor object.
    """

    permission_classes = [ProjectPermissions, IsAuthenticated]
    serializer_class = ContributorSerializer

    def get_queryset(self):
        queryset = Contributor.objects.filter(pk=self.kwargs['pk'])
        return queryset


class IssueList(ListAPIView, CreateAPIView):

    """
    API endpoint that allows listing and creation of issues for a project.

    Inherits from ListAPIView and CreateAPIView.
    Requires authentication (IsAuthenticated permission) and ContributorPermissions permission to access.
    Uses the IssueSerializer for serialization.
    Returns a queryset of all Issue objects for the specified project.
    """

    permission_classes = [IsAuthenticated, ContributorPermissions]
    serializer_class = IssueSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')
        queryset = Issue.objects.filter(project=project_id)
        return queryset


class IssueDetail(RetrieveAPIView, DestroyAPIView, UpdateAPIView):

    """
    API endpoint that allows retrieval, update and deletion of an issue.

    Inherits from RetrieveAPIView, UpdateAPIView and DestroyAPIView.
    Requires authentication (IsAuthenticated permission) and CommentIssuePermissions to access.
    Uses the IssueSerializer for serialization.
    Returns a queryset of the specified Issue object.
    """

    permission_classes = [CommentIssuePermissions, IsAuthenticated]
    serializer_class = IssueSerializer

    def get_queryset(self):
        queryset = Issue.objects.filter(pk=self.kwargs['pk'])
        return queryset


class CommentList(ListAPIView, CreateAPIView):

    """
    API endpoint that allows listing and creation of comments for an issue.

    Inherits from ListAPIView and CreateAPIView.
    Requires authentication (IsAuthenticated permission) and ContributorPermissions permission to access.
    Uses the CommentSerializer for serialization.
    Returns a queryset of all Comment objects for the specified issue.
    """

    permission_classes = [IsAuthenticated, ContributorPermissions]
    serializer_class = CommentSerializer

    def get_queryset(self):
        issue_id = self.kwargs.get('issue_id')
        queryset = Comment.objects.filter(issue=issue_id)
        return queryset


class CommentDetail(RetrieveAPIView, DestroyAPIView, UpdateAPIView):

    """
    API endpoint that allows retrieval, update and deletion of a comment.

    Inherits from RetrieveAPIView, UpdateAPIView and DestroyAPIView.
    Requires authentication (IsAuthenticated permission) and CommentIssuePermissions to access.
    Uses the CommentSerializer for serialization.
    Returns a queryset of the specified Comment object.
    """

    permission_classes = [CommentIssuePermissions, IsAuthenticated]
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.filter(pk=self.kwargs['pk'])
        return queryset
