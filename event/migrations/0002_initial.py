# Generated by Django 4.2.8 on 2023-12-30 00:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chat_group', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventattendee',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='chat_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='chat_group.chatgroup'),
        ),
        migrations.AddField(
            model_name='event',
            name='members',
            field=models.ManyToManyField(related_name='events', through='event.EventAttendee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
