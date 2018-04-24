from rest_framework import serializers

from .models import *


class TournamentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tournament
        fields = ('name', 'start_date', 'end_date', 'category')


class CombatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Combat
        fields = ('date', 'loser', 'winner')


class FighterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fighter
        fields = ('id', 'url', 'alias', 'skills', 'force', 'resistance')