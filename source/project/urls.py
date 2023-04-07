from django.urls import path

from project.views import ProjectList, ProjectDetail
from project.views import ContributorList, ContributorDelete
from project.views import IssueList, IssueDetail
from project.views import CommentList

urlpatterns = [
    path('', ProjectList.as_view()),
    path('<int:pk>/', ProjectDetail.as_view()),
    path('<int:project_id>/users/', ContributorList.as_view()),
    path('<int:project_id>/users/<int:pk>/', ContributorDelete.as_view()),
    path('<int:project_id>/issues/', IssueList.as_view()),
    path('<int:project_id>/issues/<int:pk>', IssueDetail.as_view()),
    path('<int:project_id>/issues/<int:issue_id>/comments/', CommentList.as_view()),
]

