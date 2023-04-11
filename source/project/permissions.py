from rest_framework.permissions import BasePermission
from .utils import permission_users


class ProjectPermissions(BasePermission):
    
    def has_permission(self, request, view):
        return permission_users(request)