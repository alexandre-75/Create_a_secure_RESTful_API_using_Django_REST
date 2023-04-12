from rest_framework.permissions import BasePermission
from .utils import permission_users, get_contributor


"""
    Django REST Framework provides a set of permission classes that allow you to control who can access your API endpoints.

    The permission classes provided by Django REST Framework are:

    - BasePermission: 
            The base class for all permission classes. 
            It provides two methods: has_permission and has_object_permission.
    - IsAuthenticated: This permission class allows access only to authenticated users.
    - AllowAny: This permission class allows access to all users, authenticated or not.

    To use a permission class in a view, you add it to the 'permission_classes' attribute of the view. 
    For example:

        class MyView(APIView):
            permission_classes = [IsAuthenticated]
            ...
    This will restrict access to the view to authenticated users only.
"""


class ProjectPermissions(BasePermission):
    
    def has_permission(self, request, view):
        return permission_users(request)

class IsContributorList(BasePermission):
    
    def has_permission(self, request, view):
        return get_contributor(request)
    
class CommentPermissions(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        return permission_users(request, obj)