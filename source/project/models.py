from django.db import models
from accounts.models import User

class Project(models.Model):

    TYPE = [("BACK", "Back-end"), ("FRONT", "Front-end"), ("IOS", "iOS"), ("ANDROID", "Android")]

    title = models.CharField(verbose_name="project_title", max_length=255)
    description = models.CharField(verbose_name="project_description", max_length=2048)
    type = models.CharField(verbose_name="project_type", max_length=50, choices=TYPE)
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


class Contributor(models.Model):

    PERMISSION = [("CONTRIB", "Contributeur"), ("AUTHOR", "Auteur")]

    permission = models.CharField(verbose_name="contributor_permission", choices=PERMISSION, max_length=50)
    role = models.CharField(verbose_name="contributor_role", max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']


class Issue(models.Model):

    TAG = [("BUG", "Bug"), ("IMPROV", "Améliorations"), ("TASK", "Tâche")]
    PRIORITY = [("LOW", "Faible"), ("MEDIUM", "Moyenne"), ("HIGH", "Elevée")]
    STATUS = [("TODO", "A faire"), ("DEV", "En cours"), ("DONE", "Terminé")]

    title = models.CharField(verbose_name="issue_title",max_length=255)
    description = models.CharField(verbose_name="issue_description", max_length=2048)
    tag = models.CharField(verbose_name="issue_tag", max_length=6, choices=TAG)
    priority = models.CharField(verbose_name="issue_priority", max_length=6, choices=PRIORITY)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    status = models.CharField(verbose_name="issue_status", max_length=4, choices=STATUS)
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)
    assignee_user = models.ForeignKey(User,on_delete=models.CASCADE, default=author_user)
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_datetime']


class Comment(models.Model):

    description = models.CharField(max_length=2048)
    author_user = models.ForeignKey(User, on_delete=models.CASCADE)
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_datetime']