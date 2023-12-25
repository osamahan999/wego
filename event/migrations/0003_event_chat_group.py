# Generated by Django 4.2.8 on 2023-12-25 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_group', '0001_initial'),
        ('event', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='chat_group',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='chat_group.chatgroup'),
            preserve_default=False,
        ),
    ]