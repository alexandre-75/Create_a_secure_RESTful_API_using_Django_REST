from rest_framework.serializers import ModelSerializer
from project.models import Project, Contributor, Issue


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
        

class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = '__all__'
    

class IssueSerializer(ModelSerializer):

    class Meta:

        model = Issue
        fields = '__all__'

