from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from agents.models import Agent, AgentType


class AgentTypeAdmin(ImportExportModelAdmin):
    list_display = ('agent_type', )
    list_display_links = ('agent_type', )
    list_per_page = 10
    search_fields = ('agent_type',)


class AgentAdmin(ImportExportModelAdmin):
    list_display = ('user', 'agent_type', 'description')
    list_display_links = ('user', 'agent_type', 'description')
    list_per_page = 10
    search_fields = ('user', 'agent_type')
    autocomplete_fields = ('user', 'agent_type')


admin.site.register(Agent, AgentAdmin)
admin.site.register(AgentType, AgentTypeAdmin)