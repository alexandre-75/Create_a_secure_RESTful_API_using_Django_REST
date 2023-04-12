from django.urls import path

from project.views import ProjectList, ProjectDetail
from project.views import ContributorList, ContributorDelete
from project.views import IssueList, IssueDetail
from project.views import CommentList, CommentDetail

urlpatterns = [
    path('', ProjectList.as_view(), name='project_list'),
    path('<int:pk>/', ProjectDetail.as_view(), name="project_list_detail"),
    path('<int:project_id>/users/', ContributorList.as_view(), name="project_contributor_list"),
    path('<int:project_id>/users/<int:pk>/', ContributorDelete.as_view(), name="project_contributor_delete"),
    path('<int:project_id>/issues/', IssueList.as_view(), name="project_issue_list"),
    path('<int:project_id>/issues/<int:pk>/', IssueDetail.as_view(), name="project_issue_detail"),
    path('<int:project_id>/issues/<int:issue_id>/comments/', CommentList.as_view(), name="project_comment_list"),
    path('<int:project_id>/issues/<int:issue_id>/comments/<int:pk>/', CommentDetail.as_view(), name="project_comment_detail"),
]

