
from mutants.models import Stats


def get_stats() -> Stats:
    return Stats.objects.all()
