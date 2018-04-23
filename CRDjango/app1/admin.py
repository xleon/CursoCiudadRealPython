from django.contrib import admin
from app1.models import Player


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'power', 'lives', 'gems']
    list_filter = ['gender']
    search_fields = ['name']
    
admin.site.register(Player, PlayerAdmin)
