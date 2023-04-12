from django.db import models
from accounts.models import User

class Project(models.Model):
    
    """
        Basic model for a project.

        Attributes:
        ----------
        TYPE: tuple / Options for the type of project. Each option is a pair of strings.
        title: str / The title of the project.
        description: str / The description of the project.
        type: str / The type of the project.
        author_user : User / The user who created the project.

        Methods:
        ---------
        __str__(): Returns a string representing the title of the project.

    """

    TYPE = [("BACK", "Back-end"), ("FRONT", "Front-end"), ("IOS", "iOS"), ("ANDROID", "Android")]

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2048)
    type = models.CharField(max_length=50, choices=TYPE)
    author_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


class Contributor(models.Model):
    
    """
        Template for a project contributor.

        Attributes:
        ----------
        PERMISSION: tuple / Options for a contributor's permission level. Each option is a pair of strings.
        permission: str / The contributor's permission level.
        role: str / The role of the contributor in the project.
        user_id : User / The user who is a contributor.
        project_id: Project / The project the user is contributing to.

        Methods:
        ---------
        __str__(): Returns a string representing the user and the project they are contributing to.

    """

    PERMISSION = [("CONTRIB", "Contributeur"), ("AUTHOR", "Auteur")]

    permission = models.CharField(verbose_name="contributor_permission", choices=PERMISSION, max_length=50)
    role = models.CharField(verbose_name="contributor_role", max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_id')
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='project_id')

    class Meta:
        ordering = ['id']
        unique_together = ['user_id', 'project_id']
    
    def __str__(self):
        return (f"{self.user_id} contribute to the project : {self.project_id}")


class Issue(models.Model):
    
    """
        Template for an issue (problem, task or improvement) in a project.

        Attributes:
        ----------
        TAG: tuple / Options for tagging an issue. Each option is a pair of strings.
        PRIORITY: tuple / Options for the priority of an issue. Each option is a pair of strings.
        STATUS: tuple / Options for the status of an issue. Each option is a pair of strings.
        title: str / The title of the issue.
        description: str / The description of the issue.
        tag: str / The issue tag.
        priority: str / The priority of the outcome.
        project : Project / The project the issue is associated with.
        status: str / The status of the issue.
        author_user : User / The user who created the issue.
        assignee_user : User / The user to whom the issue is assigned. By default, this is the user who created the issue.
        created_datetime : datetime.datetime /The date and time the issue was created.

        Methods:
        ---------
        __str__(): Returns a string representing the title of the issue.

    """

    TAG = [("BUG", "Bug"), ("IMPROV", "Améliorations"), ("TASK", "Tâche")]
    PRIORITY = [("LOW", "Faible"), ("MEDIUM", "Moyenne"), ("HIGH", "Elevée")]
    STATUS = [("TODO", "A faire"), ("DEV", "En cours"), ("DONE", "Terminé")]

    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2048)
    tag = models.CharField(max_length=6, choices=TAG)
    priority = models.CharField(max_length=6, choices=PRIORITY)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(max_length=4, choices=STATUS)
    author_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_user')
    assignee_user = models.ForeignKey(User,on_delete=models.CASCADE, default=author_user, related_name='assignee_user')
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_datetime']
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    
    """
        Template for a comment on an issue.

        Attributes:
        ----------
        description: str / The description of the comment.
        author_user : User / The user who created the comment.
        issue : Issue / The issue on which the comment was made.
        created_datetime : datetime.datetime / The date and time the comment was created.

    """

    description = models.CharField(max_length=2048)
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_datetime']