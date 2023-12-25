from django.contrib import admin

from .models import Me


@admin.register(Me)
class MeAdmin(admin.ModelAdmin):
    pass
