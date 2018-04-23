from django.contrib import admin
from fight_game.models import *

class TournamentAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date', 'category']

class FighterAdmin(admin.ModelAdmin):
    list_display = ['alias', 'skills', 'force', 'resistance']

class CombatAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'tournament', 'date', 'winner']

admin.site.register(Tournament, TournamentAdmin)
admin.site.register(Combat, CombatAdmin)
admin.site.register(Fighter, FighterAdmin)
