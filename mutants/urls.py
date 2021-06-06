from django.conf.urls import url

from mutants.views import MutantView, StatView

urlpatterns = [
    url(
        'mutant',
        MutantView.as_view(),
        name="mutant-info"
    ),
    url(
        'stats',
        StatView.as_view(),
        name="stats-info"
    )
]
