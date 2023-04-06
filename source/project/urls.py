from django.urls import path

from project.views import ProjectList, ProjectDetail
from project.views import ContributorList, ContributorDelete

urlpatterns = [
    path('', ProjectList.as_view()),
    path('<int:pk>/', ProjectDetail.as_view()),
    path('<int:project_id>/users/', ContributorList.as_view()),
    path('<int:project_id>/users/<int:pk>', ContributorDelete.as_view()),
]

