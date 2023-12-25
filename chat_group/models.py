from django.db import models
from django.db.models import IntegerChoices


class StatusEnum(IntegerChoices):
    UNKNOWN = 0, "Unknown"
    DRAFT = 1, "Draft"
    PUBLISHED = 2, "Published"
    ARCHIVED = 3, "Archived"
    DELETED = 4, "Deleted"


class ChatGroup(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.IntegerField(choices=StatusEnum.choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
