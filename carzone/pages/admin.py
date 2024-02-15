from django.contrib import admin

from carzone.pages.models import Team

admin.site.register(Team)

# 2nd option for registering
# @admin.register(Team)
# class TeamAdmin(admin.ModelAdmin):
#     pass