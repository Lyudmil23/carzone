from django.contrib import admin
from django.utils.html import format_html

from carzone.pages.models import Team


class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.photo.url))

    thumbnail.short_description = 'Photo'

    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'created_at')
    list_display_links = ('id', 'thumbnail', 'first_name')
    search_fields = ('first_name', 'last_name', 'designation')
    list_filter = ('designation', )


admin.site.register(Team, TeamAdmin)

# 2nd option for registering
# @admin.register(Team)
# class TeamAdmin(admin.ModelAdmin):
#     list_display = ('id', 'first_name', 'designation', 'created_at')
#     list_display_links = ('id', 'first_name')