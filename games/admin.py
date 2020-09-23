from django.contrib import admin

from .models import Game, Level, Mode, MatchType, Match

admin.site.register(Game)
admin.site.register(Level)
admin.site.register(Mode)
admin.site.register(MatchType)
admin.site.register(Match)
