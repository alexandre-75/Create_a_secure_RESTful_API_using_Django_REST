from rest_framework import permissions
from .models import Project, Contributor

def permission_users(request):
    
    if request.method in permissions.SAFE_METHODS:
        return get_contributor(request)
    return get_project(request).author_user == request.user
    

def get_contributor(request):
    
    contributors = []
    for user in Contributor.objects.filter(project_id=get_project(request)):
        if user.user_id:
            contributors.append(user.user_id)

    if request.user in contributors:
        return True

def get_project(request):
    try:
        project_id = request.parser_context["kwargs"]["project_id"]
    except KeyError:
        project_id = request.parser_context["kwargs"]["pk"]
    projet = Project.objects.get(id=project_id)
    return projet