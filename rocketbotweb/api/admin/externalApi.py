from django.contrib import admin
from ..models import ExternalApi


def delete_line(queryset):
    queryset.delete()


class ExternalApiAdmin(admin.ModelAdmin):
    fields = ['name', 'url']
    list_display = ('id', 'name', 'url')
    search_fields = ['id', 'name']
    list_display_links = ['name']

    actions = [delete_line]


admin.site.register(ExternalApi, ExternalApiAdmin)
