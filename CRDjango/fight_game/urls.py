from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'fighters', views.FighterViewSet)
router.register(r'tournaments', views.TournamentViewSet)
router.register(r'combats', views.CombatViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('tournaments/', views.TournamentsView.as_view()),
    path('fighters/', views.FightersView.as_view()),
    path('combats/', views.CombatsView.as_view()),
    path('', views.GameIndex.as_view())
]
