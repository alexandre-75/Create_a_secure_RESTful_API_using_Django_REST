from rest_framework.serializers import ModelSerializer
from project.models import Project, Contributor, Issue, Comment

"""
    serializers are a key component of Django REST Framework,
    that manage the conversion of data between Python and JSON formats for REST APIs.
"""


class ProjectSerializer(ModelSerializer):
    
    """
    Serializer for the Project model.

    Uses the ModelSerializer class provided by Django REST Framework,
    for converting Project objects to JSON and vice versa.
    """
     
    class Meta:
        model = Project
        fields = '__all__'
        

class ContributorSerializer(ModelSerializer):
 
    """
    Serializer for the Contributor model.

    Uses the ModelSerializer class provided by Django REST Framework,
    for converting Contributor objects to JSON and vice versa.
    """

    class Meta:
        model = Contributor
        fields = '__all__'
    

class IssueSerializer(ModelSerializer):
    
    """
    Serializer for the Issue model.

    Uses the ModelSerializer class provided by Django REST Framework,
    for converting Issue objects to JSON and vice versa.
    """

    class Meta:

        model = Issue
        fields = '__all__'
        
class CommentSerializer(ModelSerializer):
    
    """
    Serializer for the Comment model.

    Uses the ModelSerializer class provided by Django REST Framework,
    for converting Comment objects to JSON and vice versa.
    """

    class Meta:

        model = Comment
        fields = '__all__'

