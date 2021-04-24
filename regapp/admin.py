from django.contrib import admin
from .models import Team
# Register your model
class TeamAdmin(admin.ModelAdmin):
    list_display = ('collegename', 'teamname', 'created_at')
admin.site.register(Team, TeamAdmin)