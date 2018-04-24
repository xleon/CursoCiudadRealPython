from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from django.views import View
from rest_framework import viewsets
from .serializers import *

from .models import Combat, Tournament, Fighter


class GameIndex(TemplateView):
    """
    Una página con torneos y jugadores del torneo de forma anidada.
    Debajo ponemos lista de combates
    """
    template_name = "game_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tournaments'] = Tournament.objects.all()
        context['combats'] = Combat.objects.order_by('-date')
        context['fighters'] = Fighter.objects.all()
        return context


class TournamentsView(TemplateView):
    template_name = "tournaments.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tournaments'] = Tournament.objects.all()
        return context


class FightersView(View):
    def get(self, request):
        return HttpResponse('Luchadores')


class CombatsView(ListView):
    model = Combat
    template_name = 'combats.html'


"""
def fighters(request):
    return HttpResponse('Luchadores')
"""


class FighterViewSet(viewsets.ModelViewSet):
    queryset = Fighter.objects.all()
    serializer_class = FighterSerializer


class TournamentViewSet(viewsets.ModelViewSet):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class CombatViewSet(viewsets.ModelViewSet):
    queryset = Combat.objects.all()
    serializer_class = CombatSerializer


