from rest_framework import permissions
from .models import Project, Contributor

def permission_users(request, obj=None):

    """
    Determines if the user has permission to access the view, based on the request method and object.

    Args:
        request: The incoming request.
        obj: The object being accessed.

    Returns:
        True if the user has permission, False otherwise.
    """

    if request.method in permissions.SAFE_METHODS:
        return get_contributor(request)
    if obj:
        return obj.author_user == request.user
    return get_project(request).author_user == request.user


def get_contributor(request):

    """
    Determines if the user is a contributor to the project.

    Args:
        request: The incoming request.

    Returns:
        True if the user is a contributor, False otherwise.
    """

    contributors = []
    for user in Contributor.objects.filter(project_id=get_project(request)):
        if user.user_id:
            contributors.append(user.user_id)

    if request.user in contributors:
        return True


def get_project(request):

    """
    Gets the project based on the request.

    Args:
        request: The incoming request.

    Returns:
        The project associated with the request.
    """

    try:
        project_id = request.parser_context["kwargs"]["project_id"]
    except KeyError:
        project_id = request.parser_context["kwargs"]["pk"]
    project = Project.objects.get(id=project_id)
    return project
