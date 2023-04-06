from django.db import models
from accounts.models import User

class Project(models.Model):

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

    description = models.CharField(max_length=2048)
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_datetime']