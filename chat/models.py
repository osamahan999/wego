from django.db import models

from chat_group.models import ChatGroup
from person.models import Person


class Chat(models.Model):
    id = models.AutoField(primary_key=True)
    chat_group = models.ForeignKey(ChatGroup, on_delete=models.PROTECT)
    author = models.ForeignKey(Person, on_delete=models.PROTECT)
    message_text = models.CharField(max_length=450)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
