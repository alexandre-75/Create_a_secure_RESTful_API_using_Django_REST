from rest_framework.permissions import BasePermission
from .utils import permission_users, get_contributor


class ProjectPermissions(BasePermission):
    
    def has_permission(self, request, view):
        return permission_users(request)

class IsContributorList(BasePermission):
    
    def has_permission(self, request, view):
        return get_contributor(request)