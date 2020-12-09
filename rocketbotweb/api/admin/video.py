from django.contrib import admin
from ..models.video import Video


def delete_line(queryset):
    queryset.delete()


class VideoAdmin(admin.ModelAdmin):
    fields = ['name', 'width', 'height', 'frames', 'frame_rate', 'url', 'first_frame', 'last_frame']
    list_display = ('id', 'name', 'width', 'height', 'frames', 'url')
    search_fields = ['id', 'name', 'frames']
    list_display_links = ['name']

    actions = [delete_line]


admin.site.register(Video, VideoAdmin)
